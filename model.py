import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as plticker
class model:

    def __init__(self, file_name, img):

        self.image = plt.imread(img)
        # self.df = pd.read_csv(file_name,
        #               names=["frame", "x", "y", "obj", "size", "seq", "tbd1", "tbd2", "tbd3",
        #                      "filename", "time", "path_time", "delta_time", "tbd4"],
        #               usecols=[ "x", "y", "obj", "seq", "filename", "time", "path_time", "delta_time"],
        #               parse_dates=["time"])

        self.df = pd.read_pickle(file_name)

        # self.ordering_data()
        # self.optimize_data()

        self.current_df = self.df
        self.df_for_filter_Square = pd.DataFrame({"x": [], "y": [], "obj": [], "seq": [],
                                                  "filename": [], "time": [], "path_time": [], "delta_time": []})

    def ordering_data(self):

        self.df['time'] = self.df['time'] + pd.to_timedelta(self.df['delta_time'])
        self.df = self.df.drop(['delta_time', 'path_time'], axis=1)

    def optimize_data(self):

        df_obj = self.df.select_dtypes(include=['object']).copy()
        converted_obj = pd.DataFrame()

        for col in df_obj.columns:
            num_unique_values = len(df_obj[col].unique())
            num_total_values = len(df_obj[col])
            if num_unique_values / num_total_values < 0.5:
                converted_obj.loc[:, col] = df_obj[col].astype('category')
            else:
                converted_obj.loc[:, col] = df_obj[col]

        compare_obj = pd.concat([df_obj.dtypes, converted_obj.dtypes], axis=1)
        compare_obj.columns = ['before', 'after']
        compare_obj.apply(pd.Series.value_counts)
        self.df[converted_obj.columns] = converted_obj

        df_int = self.df.select_dtypes(include=['int64'])
        converted_int = df_int.apply(pd.to_numeric, downcast='unsigned')
        self.df[converted_int.columns] = converted_int

        self.df.drop_duplicates()

    def to_time_filter(self, start_date, end_date):

        self.current_df = self.current_df[(self.current_df.time.dt.time > start_date.time())\
                                  & (self.current_df.time.dt.time <= end_date.time())]

    def to_date_filter(self, specific_date, start_time, end_time):

        self.current_df = self.current_df[(self.current_df.time.dt.time >= start_time.time())\
                            & (self.current_df.time.dt.time <= end_time.time())\
                            & (self.current_df.time.dt.date == specific_date.date())]


    def area_filter(self, top_left, bottom_right):

        self.current_df = self.current_df[(self.current_df.x.between(int(top_left[0]), int(bottom_right[0])))\
                                          & (self.current_df.y.between(int(top_left[1]), int(bottom_right[1])))]


    def for_filter_Square(self, top_left, bottom_right):

        return self.current_df[(self.current_df.x.between(int(top_left[0]), int(bottom_right[0]))) \
                                          & (self.current_df.y.between(int(bottom_right[1]), int(top_left[1])))]


    def filter_Square(self, locaition_list):
       im_size = self.image.shape
       width = im_size[1]
       height = im_size[0]
       num_segmentation = 10

       for i in locaition_list:
           r = i // num_segmentation
           c = i - (r * num_segmentation)
           top_left = (c * width / num_segmentation , (r + 1) * height / num_segmentation)
           bottom_right = ((c + 1) * width / num_segmentation, r * height / num_segmentation)
           
           frames = [self.df_for_filter_Square, self.for_filter_Square(top_left, bottom_right)]
           self.df_for_filter_Square = pd.concat(frames, sort = True)

       self.current_df = self.df_for_filter_Square
       self.df_for_filter_Square = pd.DataFrame({"x": [], "y": [], "obj": [], "seq": [],
                                                    "filename": [], "time": [], "path_time": [], "delta_time": []})
    def drow_grid(self):

        # Load the image
        img =self.image
        fig = plt.figure(figsize=(15, 10))
        ax = fig.add_subplot(111)

        im_size = self.image.shape
        width = im_size[1]
        height = im_size[0]

        myInterval_w = width // 10
        myInterval_h = height // 10

        loc_w = plticker.MultipleLocator(base=myInterval_w)
        loc_h = plticker.MultipleLocator(base=myInterval_h)

        ax.xaxis.set_major_locator(loc_w)
        ax.yaxis.set_major_locator(loc_h)

        # Add the grid
        ax.grid(which='major', axis='both', linestyle='-', color="k")

        # Add the image
        ax.imshow(img)

        # Find number of gridsquares in x and y direction
        nx = abs(int(float(ax.get_xlim()[1] - ax.get_xlim()[0]) / float(myInterval_w)))
        ny = abs(int(float(ax.get_ylim()[1] - ax.get_ylim()[0]) / float(myInterval_h)))

        # Add some labels to the gridsquares
        for j in range(ny):
            y = myInterval_h / 2 + j * myInterval_h
            for i in range(nx):
                x = myInterval_w / 2. + float(i) * myInterval_w
                ax.text(x, y, '{:d}'.format(i + j * nx), color='k', ha='center', va='center')

        # Show the result
        plt.imshow(img)
        plt.show()