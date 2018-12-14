import logging

import seaborn
import matplotlib.pyplot as plt
from model import model
from view import view
import pandas as pd
from gui import Gui
CONST_SQUERS = 10

logging.basicConfig(
        format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

class controller:

    def __init__(self, df_path, p_path):
        self.m_model = model(df_path, p_path)
        commands = {'time': self.run_time, 'draw': self.draw, 'clear': self.clear, 'area_squers': self.area_squers,
                    'date': self.date, 'one_by_one': self.draw}
        self.gui_view = Gui(commands)
        self.filters = {'time': [], 'date': [], 'area': [], 'area_squers': []}

    def run_time(self):
        # time_fltr = self.gui_view.get_time_input()
        #
        # start, end = time_fltr.split(' ')

        start = "07:00:00"
        end = "07:02:00"

        # logger.info(f"> on #{time_fltr}, start {start}, end {end}")
        try:
            start_time = pd.to_datetime(start)
            end_time = pd.to_datetime(end)

            update = f"searching for:\nstart: {start},\nend: {end}"
            self.gui_view.set_status(update)

            self.m_model.to_time_filter(start_time, end_time)

            self.filters['time'].append((start_time, end_time))

        except ValueError:

            logger.info(f"> on time filter #invalid time ")

            update = f"value error, time filter not saved"
            self.gui_view.set_status(update)

    def area_squers(self):


        x1, y1, x2, y2 = self.gui_view.get_cor().split(',')
        logger.info(f"> on area_squers filter {x1, y1, x2, y2} ")
        self.m_model.area_filter((x1, y1),(x2, y2))

    def date(self):

        date, start, end = self.gui_view.get_date().split(' ')
        logger.info(f"> on area_squers filter {date, start, end} ")
        update = f"searching for:\ndate {date}\nstart: {start},\nend: {end}"
        try:
            date = pd.to_datetime(date)
            start = pd.to_datetime(start)
            end = pd.to_datetime(end)


            self.gui_view.set_status(update)

            self.m_model.to_date_filter(date, start, end)

        except ValueError:

            logger.info(f"> on date filter #invalid date ")

            update = f"value error, time filter not saved"
            self.gui_view.set_status(update)


    def draw(self):

            table = self.m_model.current_df.groupby(['filename', 'obj']).size().head(2000)
            df_by_obj = self.m_model.df.set_index(['filename', 'obj']).sort_index()

# ​            self.gui_view.draw_plt(table, df_by_obj, self.m_model.image)

            if self.gui_view.is_checked_is_checked():
               self.gui_view.draw_one_by_one(table,df_by_obj,self.m_model.image)
            else:
                self.gui_view.draw_plt(table,df_by_obj,self.m_model.image)

    def run(self):

        self.gui_view.master.mainloop()

    def clear(self):

        logger.info(f"> on clear")

        update = f"clear filters"
        self.gui_view.set_status(update)
        self.m_model.clear()
        self.filters = {'time': [], 'date': [], 'area': [], 'areas_squers': []}



        # com = self.view.run(self.m_model.image, self.m_model.df, self.m_model.current_df)
        #
        # while(com[0] != "end"):
        #     if com[0] == "clear":
        #         self.m_model.clear()
        #
        #     elif com[0] == "area":
        #         self.m_model.area_filter(com[1], com[2])
        #
        #     elif com[0] == "time":
        #         if len(com) == 3:
        #             self.m_model.to_time_filter(com[1], com[2])
        #
        #     elif com[0] == "date":
        #         if len(com) == 4:
        #             self.m_model.to_date_filter(com[1], com[2], com[3])
        #
        #     elif com[0] == "area_squers":
        #         self.m_model.filter_Square(com[1])
        #
        #     elif com[0] == "draw_one_by_one":
        #         self.view.draw_one_by_one(self.m_model.df, self.m_model.current_df, self.m_model.image)
        #
        #     elif com[0] == "draw":
        #         self.view.draw(self.m_model.df, self.m_model.current_df, self.m_model.image)
        #
        #     elif com[0] == "heatmap":
        #            seaborn.heatmap(self.m_model.df)
        #            plt.show()
        #
        #     com = self.view.run(self.m_model.image, self.m_model.df, self.m_model.current_df)
