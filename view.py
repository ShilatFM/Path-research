import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import pandas as pd

class view:

    def __init__(self):
        self.filters = {'time': [], 'date': [], 'area': [], 'areas_squers': []}

    def draw(self, original_df, current_df, img):

        print("im in draw")
        table = current_df.groupby(['filename', 'obj']).size().head(200)
        df_by_obj = original_df.set_index(['filename', 'obj']).sort_index()

        plt.imshow(img)

        for t in table.index:
            s_o = df_by_obj.loc[t]
            s_o.sort_values('seq')
            plt.plot(s_o.x, s_o.y, label = t[1])
        plt.legend(loc=9, bbox_to_anchor=(1.1, 1))

        plt.pause(0.5)
        plt.gcf().clear()

    def draw_one_by_one(self, original_df, current_df, img):

        print("im in draw_one_by_one")

        # flag = False
        # if pause == -1:
        #     flag = True

        table = current_df.groupby(['filename', 'obj']).size()
        df_by_obj = original_df.set_index(['filename', 'obj']).sort_index()

        for t in table.index:
            s_o = df_by_obj.loc[t]
            s_o.sort_values('seq')
            plt.imshow(img)

            m = f"video:\n{t[0]}\nobject:\n{t[1]}\nstart:\n{s_o.time.max()}\n\
            end:\n{s_o.time.min()}\n perfomed on {len(s_o)}\n frames"

            plt.plot(s_o.x, s_o.y, label=m)
            plt.legend(bbox_to_anchor=(1.1, -0.4), loc='lower right', fontsize=9)
            plt.pause(0.4)
            plt.gcf().clear()
            # if flag:
            # next = input("next?: ")
            # if next != 'y':
            #     break

    def drow_grid(self, img):

            fig = plt.figure(figsize=(15, 10))
            ax = fig.add_subplot(111)

            im_size = img.shape
            width = im_size[1]
            height = im_size[0]

            myInterval_w = width // 10
            myInterval_h = height // 10

            loc_w = plticker.MultipleLocator(base=myInterval_w)
            loc_h = plticker.MultipleLocator(base=myInterval_h)

            ax.xaxis.set_major_locator(loc_w)
            ax.yaxis.set_major_locator(loc_h)

            ax.grid(which='major', axis='both', linestyle='-', color="k")

            ax.imshow(img)

            nx = abs(int(float(ax.get_xlim()[1] - ax.get_xlim()[0]) / float(myInterval_w)))
            ny = abs(int(float(ax.get_ylim()[1] - ax.get_ylim()[0]) / float(myInterval_h)))

            for j in range(ny):
                y = myInterval_h / 2 + j * myInterval_h
                for i in range(nx):
                    x = myInterval_w / 2. + float(i) * myInterval_w
                    ax.text(x, y, '{:d}'.format(i + j * nx), color='k', ha='center', va='center')

            plt.imshow(img)
            plt.pause(0.4)
            plt.gcf().clear()

    def run(self, img, df, current_df):
        command = input("enter command:")

        if not command:
            print("goodbye")
            return ["end"]

        if command == '/draw':
            if len(current_df) < 20000:
                answer = input("if you want draw_one_by_one enter /y")
                if answer == "/y":
                    return ["draw_one_by_one"]

                else:
                    return ["draw"]

            return ["draw"]


        elif command == '/time':
            start = input("enter start time in the following format: hh:mm:ss\n")
            try:
                start_time = pd.to_datetime(start)
            except ValueError:
                print("value error, time filter not saved")
                return ["time"]
            end = input("enter end time in the following format: hh:mm:ss\n")
            try:
                end_time = pd.to_datetime(end)
            except ValueError:
                print("value error, time filter not saved")
                return ["time"]
            self.filters['time'].append((start_time, end_time))
            return ["time", start_time, end_time]

        elif command == '/date':
            date = input("enter date in the following format: yyyy-mm-dd")
            try:
                my_date = pd.to_datetime(date)
            except ValueError:
                print("value error, date filter not saved")
                return ["date"]
            start = input("enter start time in the following format: hh:mm:ss\n")
            try:
                start_time = pd.to_datetime(start)
            except ValueError:
                print("value error, date filter not saved")
                return ["date"]
            end = input("enter end time in the following format: hh:mm:ss\n")
            try:
                end_time = pd.to_datetime(end)
            except ValueError:
                print("value error, date filter not saved")
                return ["date"]
            self.filters['date'].append((my_date, start_time, end_time))
            return ["date", my_date, start_time, end_time]

        elif command == '/area':
            x1 = input("enter x value for top left point")
            y1 = input("enter y value for top left point")
            x2 = input("enter x value for bottom right point")
            y2 = input("enter y value for bottom right point")
            self.filters['area'].append(((x1, y1), (x2, y2)))
            return ["area", (x1, y1), (x2, y2)]

        elif command == '/area_squers':
            self.drow_grid(img)
            print("to stop adding squers press enter")
            while (True):
                x = input(f"enter next squere between 0 and 99\n")
                if not x:
                    break
                try:
                    int(x)
                except ValueError:
                    print("value error, you must enter ints\n")
                    continue
                if (0 <= int(x) <= 99):
                    self.filters['areas_squers'].append(int(x))
                else:
                    print("Value error, squere out of range\n")
            return ["area_squers", self.filters['areas_squers']]

        elif command == '/show_filters':
            if len(self.filters['time']) != 0:
                print('time filters:')
                for now_time in self.filters['time']:
                    print(f"start: {now_time[0]}")
                    print(f"end: {now_time[1]}\n")

            if len(self.filters['date']) != 0:
                print('date filters:')
                for now_date in self.filters['date']:
                    print(f"date: {now_date[0]}")
                    print(f"start time: {now_date[1]}")
                    print(f"end time: {now_date[2]}\n")

            if len(self.filters['area']) != 0:
                print('area filters:')
                for now_area in self.filters['area']:
                    print(f"top left point: {now_area[0]}")
                    print(f"bottom right point: {now_area[1]}\n")

            if len(self.filters['areas_squers']) != 0:
                print('area_squers filters:')
                for now_area_squeres in self.filters['areas_squers']:
                    print(f"squere: {now_area_squeres}\n")

            return ["show_filters"]

        elif command == '/clear':
            self.filters = {'time': [], 'date': [], 'area': [], 'areas_squers': []}
            return ["clear"]

        else:
            print("invalid command")
            return ["invalid command"]

