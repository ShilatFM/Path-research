
import logging
import tkinter as tk
import matplotlib.ticker as plticker

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

logging.basicConfig(
        format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

class Gui:

    def __init__(self, defs):

        master = tk.Tk()
        self.master = master
        self.com = defs
        self.basic_gui()
        self.init_canvas()
        self.init_enries()
        self.init_buttons()
        self.init_lables()
        self.check_buttons()




    def basic_gui(self):

        self.master_frame = tk.Frame(self.master, bg='white')
        self.master_frame.grid()

    def check_buttons(self):

        self.one_by_one_var = tk.IntVar(0)
        self.one_by_one = tk.Checkbutton(self.master_frame, text="one by one", bg='white', variable=self.one_by_one_var)
        self.one_by_one.grid(row=12, column=5, sticky=tk.W, padx=5, pady=5)


    def init_lables(self):

        tk.Label(self.master_frame, text="Enter start\nand end time", bg='white').grid(row=1, column=5,
                                                                                       sticky=tk.W, padx=5, pady=5)

        tk.Label(self.master_frame, text="Enter (x1,y1)\n(x2, y2)", bg='white').grid(row=3, column=5, sticky=tk.W,
                                                                                     padx=5, pady=5)

        tk.Label(self.master_frame, text="Enter squere\nnumber", bg='white').grid(row=5, column=5, sticky=tk.W,
                                                                                  padx=5, pady=5)

        tk.Label(self.master_frame, text="Enter date\n+ start and \nend hour", bg='white').grid(row=7, column=5,
                                                                                                sticky=tk.W, padx=5,
                                                                                                pady=5)

        self.status = tk.Label(self.master_frame,
                               text="here you will see all messages", width=50,
                               height=14, bg='white')
        self.status.grid(row=9, rowspan=6, column=0, columnspan=3, padx=5, sticky=tk.E, pady=5)

    def init_buttons(self):

        self.date_filter = tk.Button(self.master_frame, text="date filter", command=self.com['date'],
                                     width=25, height=1).grid(row=8, column=5, columnspan=2,
                                                              sticky=tk.W + tk.E + tk.N + tk.S, padx=5, pady=5)

        self.filter_time = tk.Button(self.master_frame, text="time filter", command=self.com['time'],
                                     width=25, height=1).grid(row=2, column=5, columnspan=2,
                                                              sticky=tk.W + tk.E + tk.N + tk.S, padx=5, pady=5)

        self.area_filter = tk.Button(self.master_frame, text="area filter", command=self.com['area_squers'],
                                     width=25, height=1).grid(row=4, column=5, columnspan=2,
                                                              sticky=tk.W + tk.E + tk.N + tk.S, padx=5, pady=5)

        self.load_img = tk.Button(self.master_frame, text="load image", command=self.com['load_img'],
                                  width=10, height=2)
        self.load_img.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.load_data = tk.Button(self.master_frame, text="load data", command=self.com['load_data'],
                                   width=10, height=2)
        self.load_data.grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)

        self.show_grid = tk.Button(self.master_frame, text="show grid", command=self.com['show_grid'],
                                   width=45, height=1).grid(row=13, column=5, padx=1, pady=5, sticky=tk.E, columnspan=2)

        self.clear = tk.Button(self.master_frame, text="clear", command=self.com['clear'],
                               width=45, height=1).grid(row=9, column=5, padx=1, pady=5, sticky=tk.E,
                                                        columnspan=2)

        self.show_filters = tk.Button(self.master_frame, text="show filters", command=self.com['show_filters'],
                                      width=45, height=1).grid(row=10, column=5, padx=1, pady=5, sticky=tk.E,
                                                               columnspan=2)

        self.plot = tk.Button(self.master_frame, text="plot", command=self.com['draw'],
                              width=45, height=1).grid(row=11, column=5, padx=1, pady=5,
                                                       sticky=tk.E, columnspan=2)

        self.squere_area_filter = tk.Button(self.master_frame, text="squere area data",
                                            command=self.com['areas_squers'],
                                            width=25, height=1).grid(row=6, column=5, columnspan=2,
                                                                     sticky=tk.W + tk.E + tk.N + tk.S, padx=5, pady=5)

    def init_enries(self):

        self.time_input = tk.Entry(self.master_frame)
        self.time_input.grid(row=1, column=6, sticky=tk.E, padx=5, pady=5)

        self.area_input = tk.Entry(self.master_frame)
        self.area_input.grid(row=3, column=6, sticky=tk.E, padx=5, pady=5)

        self.img_path = tk.Entry(self.master_frame)
        self.img_path.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        self.data_path = tk.Entry(self.master_frame)
        self.data_path.grid(row=0, column=3, sticky=tk.E, padx=5, pady=5)

        self.squere_area_input = tk.Entry(self.master_frame)
        self.squere_area_input.grid(row=5, column=6, sticky=tk.E, padx=5, pady=5)

        self.date_input = tk.Entry(self.master_frame)
        self.date_input.grid(row=7, column=6, sticky=tk.E, padx=5, pady=5)

    def init_canvas(self):

        self.fig = plt.figure(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master_frame)
        self.canvas.get_tk_widget().grid(row=1, rowspan=8, columnspan=4, padx=5, pady=5)

    def get_image_path(self):
        return self.img_path.get()

    def get_data_path(self):
        return self.data_path.get()

    def get_time_input(self):
        return self.time_input.get()

    def set_status(self, update):
        self.status['text'] = update

    def get_cor(self):
        return self.area_input.get()

    def get_date(self):
        return  self.date_input.get()

    def is_checked_is_checked(self):
        return self.one_by_one_var.get()

    def draw_grid(self, img, w_squers, h_squers):

        # self.fig = plt.figure(figsize=(5, 4))
        ax = self.fig.add_subplot(111)

        im_size = img.shape
        width = im_size[1]
        height = im_size[0]

        myInterval_w = width // w_squers
        myInterval_h = height // h_squers

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

        self.canvas.draw()
        plt.gcf().clear()

    def get_squere(self):

        return self.squere_area_input.get()



    def draw_plt(self, table, df_by_obj, img):

        plt.imshow(img)

        for t in table.index:
            s_o = df_by_obj.loc[t]
            s_o.sort_values('seq')
            plt.plot(s_o.x, s_o.y, label=t[1])

        self.canvas.draw()
        plt.gcf().clear()

    def draw_one_by_one(self, table, df_by_obj, img):

        for t in table.index:

            plt.imshow(img)
            oo = df_by_obj.loc[t]
            plt.plot(oo.x, oo.y)
            self.canvas.draw()
            self.master.after(500)
            plt.gcf().clear()
            # self.fig.clear()


