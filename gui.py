
import logging
import tkinter as tk
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

    def basic_gui(self):

        self.master_frame = tk.Frame(self.master, bg='white')
        self.master_frame.grid()

        self.load_img = tk.Button(self.master_frame, text="load image", command=self.draw_plt,
                                  width=10, height=2)
        self.load_img.grid(row=0, column = 0, sticky=tk.W, padx=5, pady=5)

        self.img_path = tk.Entry(self.master_frame)
        self.img_path.grid(row=0, column = 1, sticky=tk.W, padx=5, pady=5)

        self.load_data = tk.Button(self.master_frame, text="load data", command=self.draw_plt,
                                   width=10, height=2)
        self.load_data.grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)

        self.data_path = tk.Entry(self.master_frame)
        self.data_path.grid(row=0, column=3, sticky=tk.E, padx=5, pady=5)

        self.filter_time = tk.Button(self.master_frame, text="time filter", command=self.com['time'],
                                     width=25, height=1).grid(row=1, column=5, columnspan=2,
                                                              sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        tk.Label(self.master_frame, text="Enter start\nand end time", bg='white').grid(row=2, column=5,
                                                                                       sticky=tk.W, padx=5, pady=5)

        self.time_input = tk.Entry(self.master_frame)
        self.time_input.grid(row=2, column=6, sticky=tk.E, padx=5, pady=5)

        self.area_filter = tk.Button(self.master_frame, text="area filter", command=self.com['area_squers'],
                                     width=25, height=1).grid(row=3, column=5, columnspan=2,
                                                              sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        tk.Label(self.master_frame, text="Enter (x1,y1)\n(x2, y2)", bg='white').grid(row=4, column=5, sticky=tk.W,
                                                                                     padx=5, pady=5)

        self.area_input = tk.Entry(self.master_frame)
        self.area_input.grid(row=4, column=6, sticky=tk.E, padx=5, pady=5)

        self.squere_area_filter = tk.Button(self.master_frame, text="squere area data", command=self.com['area_squers'],
                                     width=25, height=1).grid(row=5, column=5, columnspan=2,
                                                              sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        tk.Label(self.master_frame, text="Enter squere\nnumber", bg='white').grid(row=6, column=5, sticky=tk.W,
                                                                                  padx=5, pady=5)

        self.squere_area_input = tk.Entry(self.master_frame)
        self.squere_area_input.grid(row=6, column=6, sticky=tk.E, padx=5, pady=5)

        self.date_filter = tk.Button(self.master_frame, text="date filter", command=self.com['date'],
                                     width=25, height=1).grid(row=7, column=5, columnspan=2,
                                                              sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        tk.Label(self.master_frame, text="Enter date\n+ start and \nend hour", bg='white').grid(row=8, column=5,
                                                                                    sticky=tk.W, padx=5, pady=5)

        self.date_input = tk.Entry(self.master_frame)
        self.date_input.grid(row=8, column=6, sticky=tk.E, padx=5, pady=5)

        self.status = tk.Label(self.master_frame,
                               text="here you will see all messages", width=50,
                               height=14, bg='white')
        self.status.grid(row=9, rowspan=6, column=0, columnspan=3, padx=5, sticky=tk.E, pady=5)

        self.clear = tk.Button(self.master_frame, text="clear", command=self.com['clear'],
                                     width=45, height=1).grid(row=9, column=5, padx=1, pady=5, sticky=tk.E,
                                                              columnspan=2)

        self.show_filters = tk.Button(self.master_frame, text="show filters", command=self.draw_plt,
                               width=45, height=1).grid(row=10, column=5, padx=1, pady=5, sticky=tk.E,
                                                        columnspan=2)

        self.plot = tk.Button(self.master_frame, text="plot", command=self.com['draw'],
                                      width=45, height=1).grid(row=11, column=5, padx=1, pady=5,
                                                               sticky=tk.E, columnspan=2)

        self.show_grid = tk.Button(self.master_frame, text="show grig", command=self.draw_plt,
                              width=45, height=1).grid(row=12, column=5, padx=1, pady=5, sticky=tk.E,
                                                       columnspan=2)

        self.one_by_one_var = tk.IntVar(0)
        self.one_by_one = tk.Checkbutton(self.master_frame, text="one by one", bg='white', variable=self.one_by_one_var)
        self.one_by_one.grid(row=13, column=5, sticky=tk.W, padx=5, pady=5)

        self.pause = tk.Checkbutton(self.master_frame, text="pause", bg='white')
        self.pause.grid(row=13, column=6, sticky=tk.E, padx=5, pady=5)

        self.next_plot = tk.Button(self.master_frame, text="next plot", command=self.draw_plt,
                              width=45, height=1).grid(row=14, column=5, padx=1, pady=5, sticky=tk.E, columnspan=2)

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

    def area_filter_def(self):
        area_fltr = self.area_input.get()
        print(area_fltr)

    def squere_filter_def(self):
        squere_area_fltr = self.squere_area_input.get()
        print(squere_area_fltr)

    def date_filter_def(self):
        date_fltr = self.date_input.get()
        print(date_fltr)



    def draw_plt(self, table, df_by_obj, img):

        fig = plt.figure(figsize=(5, 4))
        plt.imshow(img)

        for t in table.index:
            s_o = df_by_obj.loc[t]
            s_o.sort_values('seq')
            plt.plot(s_o.x, s_o.y, label=t[1])
        # plt.legend(loc=9, bbox_to_anchor=(1.1, 1))

        plt.pause(0.5)
        plt.gcf().clear()

        canvas = FigureCanvasTkAgg(fig, master=self.master_frame)
        canvas.show()
        canvas.get_tk_widget().grid( row = 1, rowspan = 8, columnspan=4, padx=5, pady=5)

    def draw_one_by_one(self, table, df_by_obj, img):
        print(type(img))

