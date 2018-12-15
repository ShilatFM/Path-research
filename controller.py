import logging
from time import sleep
from model import model
import pandas as pd
from gui import Gui
import matplotlib.pyplot as plt


logging.basicConfig(
        format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

class controller:

    def __init__(self):
        self.m_model = model()
        commands = {'time': self.time, 'draw': self.draw, 'clear': self.clear, 'area_squers': self.area_squers,
                    'date': self.date, 'one_by_one': self.draw, 'show_filters': self.show_filters, 'show_grid': self.show_grid,
                    'areas_squers': self.areas_squers, 'load_img': self.load_img, 'load_data': self.load_data }
        self.gui_view = Gui(commands)
        self.filters = {'time': [], 'date': [], 'area': [], 'area_squers': []}

    def run(self):

        logger.info(f"> on #run loop")

        self.gui_view.master.mainloop()

    def load_img(self):

        path = self.gui_view.get_image_path()
        logger.info(f"> on load_img -- path -- {path} ")

        try:
            if path:
                img = plt.imread(path)
                self.m_model.load_img(img)
                update = f"Image is loaded"


            else:
                update = f"Enter an image path"
            self.gui_view.set_status(update)
        except:
            update = f"No such file or directory: '{path}'"
            self.gui_view.set_status(update)


    def load_data(self):

        path = self.gui_view.get_data_path()
        logger.info(f"> on load_data -- path -- {path} ")
        try:
            if path:
                data = pd.read_pickle(path)
                self.m_model.load_data(data)
                update = f"Data is loaded"
            else:
                update = f"Enter a data path"
            self.gui_view.set_status(update)
        except:
            update = f"No such file or directory: '{path}'"
            self.gui_view.set_status(update)

    def time(self):

        time_fltr = self.gui_view.get_time_input()


        try:

            start, end = time_fltr.split(' ')
            logger.info(f"> on #{time_fltr}, start {start}, end {end}")
            start_time = pd.to_datetime(start)
            end_time = pd.to_datetime(end)

            update = f"searching for:\nstart: {start},\nend: {end}"
            self.gui_view.set_status(update)

            self.m_model.to_time_filter(start_time, end_time)

            self.filters['time'].append((start_time, end_time))

        except ValueError:

            logger.info(f"> on time filter #invalid time ")

            update = f"Value error, excepted 2 times objects, got '{time_fltr}'"
            self.gui_view.set_status(update)
        except:
            logger.info(f"> on time - no image")
            update = 'First load an image'
            self.gui_view.set_status(update)

    def area_squers(self):
        massege = self.gui_view.get_cor()

        try:

            x1, y1, x2, y2 = massege.split(',')
            logger.info(f"> on area filter {x1, y1, x2, y2} ")

            self.m_model.area_filter((int(x1), int(y1)),(int(x2), int(y2)))

            self.filters['area'].append(((x1, y1), (x2, y2)))

        except ValueError:

            update = f"Except {{x1,y1,x2,y2 format}}, got '{massege}'"
            self.gui_view.set_status(update)

        except:
            logger.info(f"> on area_squers - no image")
            update = 'First load an image'
            self.gui_view.set_status(update)


    def date(self):

        time_fltr = self.gui_view.get_date()
        try:
            date, start, end = time_fltr.split(' ')

            date = pd.to_datetime(date)
            start = pd.to_datetime(start)
            end = pd.to_datetime(end)

            logger.info(f"> on date filter {date, start, end} ")
            update = f"searching for:\ndate {date}\nstart: {start},\nend: {end}"

            self.gui_view.set_status(update)

            self.m_model.to_date_filter(date, start, end)
            self.filters['date'].append((date, start, end))
            self.gui_view.set_status(update)


        except ValueError:
            logger.info(f"> on date filter #invalid date ")
            update = f"Value error, excepted 1 date 2 times objects, got '{time_fltr}'"

            self.gui_view.set_status(update)

        except:
            logger.info(f"> on date - no image")
            update = 'First load an image'
            self.gui_view.set_status(update)

    def areas_squers(self):

        try:
            squere = int(self.gui_view.get_squere())

            logger.info(f"> on area_squers filter, num squere is --- {squere}")

            if (0 <= squere <= 99):

                self.filters['area_squers'].append(squere)
                self.m_model.filter_Square([squere])
                update = f"Search in squere -- {squere}\n"

            else:
                logger.info(f"> squere out of range")

                update = f"Value error, squere out of range\n"
                self.gui_view.set_status(update)

        except ValueError:

            logger.info(f"> value error - value is not an 'int'")
            update = f"value error, you must enter ints\n"
            self.gui_view.set_status(update)

        except:
            logger.info(f"> on areas_squers - no image")
            update = 'First load an image'
            self.gui_view.set_status(update)

    def show_grid(self):

        try:
            msg = self.gui_view.get_grid()

            if msg:
                try:
                    grid = msg.split('x')

                    self.gui_view.draw_grid(self.m_model.image, int(grid[0]), int(grid[1]))
                    update = f"Show the grid, image is dvided to {grid[0]}x{grid[1]}"
                    self.gui_view.set_status(update)
                    logger.info(f"> on show grid")

                except ValueError:

                    logger.info(f"> on show_grid - ValueError")
                    update = f'ValueError - excepted format width_squers_num,\nhigh_squers_num got {msg}'
                    self.gui_view.set_status(update)

            else:
                update = f'The defualt greed is: 5x5'
                self.gui_view.draw_grid(self.m_model.image, 5, 5)
                self.gui_view.set_status(update)

        except:
            logger.info(f"> on show_grid - no image")
            update = 'First load an image'
            self.gui_view.set_status(update)

    def draw(self):

        try:
            logger.info(f"> on draw function")

            table = self.m_model.current_df.groupby(['filename', 'obj']).size().head(90)
            logger.info(f"> len table: {len(table)}")

            df_by_obj = self.m_model.df.set_index(['filename', 'obj']).sort_index()

            if self.gui_view.is_checked_is_checked():

                update = 'Draw routes one by one'
                self.gui_view.draw_one_by_one(table,df_by_obj,self.m_model.image)

            else:

                update = 'First 200 routes'
                self.gui_view.draw_plt(table,df_by_obj,self.m_model.image)

            self.gui_view.set_status(update)

        except:
            logger.info(f"> data path or image path is missing")
            update = 'data path or image path is missing or incorrect'
            self.gui_view.set_status(update)



    def show_filters(self):

        logger.info(f"> on show_filters function")

        if len(self.filters['time']):

            update = 'time filters:'
            self.gui_view.set_status(update)

            for now_time in self.filters['time']:
                update = f"start: {now_time[0]}\nend: {now_time[1]}"
                self.gui_view.set_status(update)

        if len(self.filters['date']):

            update = f'date filters:'
            self.gui_view.set_status(update)

            for now_date in self.filters['date']:
                update = f"date: {now_date[0]}\nstart time: {now_date[1]}\nend time: {now_date[2]}"
                self.gui_view.set_status(update)

        if len(self.filters['area']):
            update = 'area filters:'
            self.gui_view.set_status(update)

            for now_area in self.filters['area']:
                sleep(2)
                update = f"top left point: {now_area[0]}\nbottom right point: {now_area[1]}"
                self.gui_view.set_status(update)

        if len(self.filters['area_squers']):
            update = 'area_squers filters:'
            self.gui_view.set_status(update)

            for now_area_squeres in self.filters['area_squers']:
                sleep(2)
                update = f"squere: {now_area_squeres}\n"
                self.gui_view.set_status(update)


    def clear(self):
        try:
            logger.info(f"> on clear")

            update = f"clear filters"
            self.gui_view.set_status(update)
            self.m_model.clear()
            self.filters = {'time': [], 'date': [], 'area': [], 'area_squers': []}

        except:

            logger.info(f"> on clear - no image")
            update = 'First load an image'
            self.gui_view.set_status(update)

