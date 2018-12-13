import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MyFirstGUI:

    def __init__(self, master):

        self.master = master

        self.basic_guy()

    def basic_guy(self):

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

        self.filter_time = tk.Button(self.master_frame, text="time filter", command=self.draw_plt,
                                     width=25, height=1).grid(row=1, column=5, columnspan=2,
                                                              sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        tk.Label(self.master_frame, text="Enter start\nend end time", bg='white').grid(row=2, column=5, sticky=tk.W, padx=5, pady=5)

        self.time_input = tk.Entry(self.master_frame).grid(row=2, column=6, sticky=tk.E, padx=5, pady=5)

        self.area_filter = tk.Button(self.master_frame, text="area filter", command=self.draw_plt,
                                     width=25, height=1).grid(row=3, column=5, columnspan=2,
                                                              sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        tk.Label(self.master_frame, text="Enter (x1,y1)\n(x2, y2)", bg='white').grid(row=4, column=5, sticky=tk.W, padx=5, pady=5)

        self.area_label = tk.Entry(self.master_frame).grid(row=4, column=6, sticky=tk.E, padx=5, pady=5)

        self.squere_area_filter = tk.Button(self.master_frame, text="squere area data", command=self.draw_plt,
                                     width=25, height=1).grid(row=5, column=5, columnspan=2,
                                                              sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        tk.Label(self.master_frame, text="Enter squere\nnumber", bg='white').grid(row=6, column=5, sticky=tk.W, padx=5, pady=5)

        self.squere_area_label = tk.Entry(self.master_frame).grid(row=6, column=6, sticky=tk.E, padx=5, pady=5)

        self.date_filter = tk.Button(self.master_frame, text="date filter", command=self.draw_plt,
                                     width=25, height=1).grid(row=7, column=5, columnspan=2,
                                                              sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

        tk.Label(self.master_frame, text="Enter date\n+ start and \nend hour", bg='white').grid(row=8, column=5,
                                                                                    sticky=tk.W, padx=5, pady=5)

        self.date_label = tk.Entry(self.master_frame).grid(row=8, column=6, sticky=tk.E, padx=5, pady=5)

        self.status = tk.Label(self.master_frame,
                               text="here you will see all messages", width=50,
                               height=14, bg='white').grid(row=9, rowspan=6, column=0, columnspan=3, padx=5, sticky=tk.E, pady=5)

        self.clear = tk.Button(self.master_frame, text="clear", command=self.draw_plt,
                                     width=45, height=1).grid(row=9, column=5, padx=1, pady=5, sticky=tk.E, columnspan=2)

        self.show_filters = tk.Button(self.master_frame, text="show filters", command=self.draw_plt,
                               width=45, height=1).grid(row=10, column=5, padx=1, pady=5, sticky=tk.E, columnspan=2)

        self.plot = tk.Button(self.master_frame, text="plot", command=self.draw_plt,
                                      width=45, height=1).grid(row=11, column=5, padx=1, pady=5, sticky=tk.E, columnspan=2)

        self.show_grid = tk.Button(self.master_frame, text="show grig", command=self.draw_plt,
                              width=45, height=1).grid(row=12, column=5, padx=1, pady=5, sticky=tk.E, columnspan=2)

        self.one_by_one = tk.Checkbutton(self.master_frame, text="one by one", bg='white').grid(row=13, column=5, sticky=tk.W, padx=5, pady=5)
        self.pause = tk.Checkbutton(self.master_frame, text="pause", bg='white').grid(row=13, column=6, sticky=tk.E, padx=5, pady=5)

        self.next_plot = tk.Button(self.master_frame, text="next plot", command=self.draw_plt,
                              width=45, height=1).grid(row=14, column=5, padx=1, pady=5, sticky=tk.E, columnspan=2)

    def draw_plt(self):

        image = plt.imread('data/paths0.png')
        fig = plt.figure(figsize=(5, 4))
        plt.imshow(image)

        canvas = FigureCanvasTkAgg(fig, master=self.master_frame)
        canvas.show()
        canvas.get_tk_widget().grid( row = 1, rowspan = 8, columnspan=4, padx=5, pady=5)



root = tk.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()