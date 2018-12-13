from model import model
from view import view
import pandas as pd
CONST_SQUERS = 10
class controller:

    def __init__(self, df_path, p_path):
        self.m_model = model(df_path, p_path)
        self.view = view()

    def run(self):
        filters = {'time': [], 'date': [], 'area': [], 'areas_squers': []}
        while (True):
            command = input("enter command:")

            if not command:
                break

            if command == '/draw':

                if len(self.m_model.current_df) < 50000:
                    answer = input("if you want draw_one_by_one enter /y else enter /n:")
                    if answer == "/y":
                        self.view.draw_one_by_one(self.m_model.df, self.m_model.current_df, self.m_model.image)
                    else:
                        self.view.draw(self.m_model.df, self.m_model.current_df, self.m_model.image)
                else:
                    self.view.draw(self.m_model.df, self.m_model.current_df, self.m_model.image)

            elif command == '/time':
                start = input("enter start time in the following format: hh:mm:ss\n")
                try:
                    start_time = pd.to_datetime(start)
                except ValueError:
                    print("value error, time filter not saved")
                    continue
                end = input("enter end time in the following format: hh:mm:ss\n")
                try:
                    end_time = pd.to_datetime(end)
                except ValueError:
                    print("value error, time filter not saved")
                    continue
                filters['time'].append((start_time, end_time))
                self.m_model.to_time_filter(start_time, end_time)
                self.view.draw(self.m_model.df, self.m_model.current_df, self.m_model.image)

            elif command == '/date':
                date = input("enter date in the following format: yyyy-mm-dd")
                try:
                    my_date = pd.to_datetime(date)
                except ValueError:
                    print("value error, date filter not saved")
                    continue
                start = input("enter start time in the following format: hh:mm:ss\n")
                try:
                    start_time = pd.to_datetime(start)
                except ValueError:
                    print("value error, date filter not saved")
                    continue
                end = input("enter end time in the following format: hh:mm:ss\n")
                try:
                    end_time = pd.to_datetime(end)
                except ValueError:
                    print("value error, date filter not saved")
                    continue
                filters['date'].append((my_date, start_time, end_time))
                self.m_model.to_date_filter(my_date, start_time, end_time)
                self.view.draw(self.m_model.df, self.m_model.current_df, self.m_model.image)

            elif command == '/area':
                x1 = input("enter x value for top left point")
                y1 = input("enter y value for top left point")
                x2 = input("enter x value for bottom right point")
                y2 = input("enter y value for bottom right point")
                filters['area'].append(((x1, y1), (x2, y2)))
                self.m_model.area_filter((x1, y1), (x2, y2))
                self.view.draw(self.m_model.df, self.m_model.current_df, self.m_model.image)


            elif command == '/area_squers':
                self.m_model.drow_grid()
                print("to stop adding squers press enter")
                while (True):
                    x = input(f"enter first squere between 0 and 99\n")
                    if not x:
                        break
                    try:
                        int(x)
                    except ValueError:
                        print("value error, you must enter ints\n")
                        continue
                    if (0 <= int(x) <= 99):
                        filters['areas_squers'].append(int(x))
                    else:
                        print("Value error, squere out of range\n")
                self.m_model.filter_Square(filters['areas_squers'])
                self.view.draw(self.m_model.df, self.m_model.current_df, self.m_model.image)


            elif command == '/show_filters':
                if len(filters['time']) != 0:
                    print('time filters:')
                    for now_time in filters['time']:
                        print(f"start: {now_time[0]}")
                        print(f"end: {now_time[1]}\n")

                if len(filters['date']) != 0:
                    print('date filters:')
                    for now_date in filters['date']:
                        print(f"date: {now_date[0]}")
                        print(f"start time: {now_date[1]}")
                        print(f"end time: {now_date[2]}\n")

                if len(filters['area']) != 0:
                    print('area filters:')
                    for now_area in filters['area']:
                        print(f"top left point: {now_area[0]}")
                        print(f"bottom right point: {now_area[1]}\n")

                if len(filters['areas_squers']) != 0:
                    print('area_squers filters:')
                    for now_area_squeres in filters['areas_squers']:
                        print(f"squere: {now_area_squeres}\n")

            elif command == '/clear':
                self.m_model.clear()
                filters = {'time': [], 'date': [], 'area': [], 'areas_squers': []}

            else:
                print("imvalid command")

        print("goodbye")