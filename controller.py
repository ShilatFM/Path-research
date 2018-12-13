# from model import model
from model import model
from view import view
import pandas as pd
CONST_SQUERS = 10
filters = {'time': [] , 'date': [], 'area': [], 'areas_squers': []}
class controller:

    def __init__(self, df_path, p_path):
        self.m_model = model(df_path, p_path)
        self.view = view()

    def run(self):

        command = input("enter command:")

        while (command):
            if command == '/draw':
                if len(self.m_model.current_df) < 20:
                    answer = input("if you want draw_one_by_one enter /y else enter /n:")
                    if answer == "/y":
                        self.view.draw_one_by_one(self.m_model.df, self.m_model.current_df, self.m_model.image)
                    else:
                        self.view.draw(self.m_model.df, self.m_model.current_df, self.m_model.image)
                else:
                    self.view.draw(self.m_model.df, self.m_model.current_df, self.m_model.image)

            elif command == '/time':
                start = input("enter start time in the following format: hh:mm:ss\n")
                start_time = pd.to_datetime(start)
                end = input("enter end time in the following format: hh:mm:ss\n")
                end_time = pd.to_datetime(end)
                self.m_model.to_time_filter(start_time, end_time)
                self.view.draw(self.m_model.df, self.m_model.current_df, self.m_model.image)

            elif command == '/date':
                date = input("enter date in the following format: yyyy-mm-dd")
                my_date = pd.to_datetime(date)
                start = input("enter start time in the following format: hh:mm:ss\n")
                start_time = pd.to_datetime(start)
                end = input("enter end time in the following format: hh:mm:ss\n")
                end_time = pd.to_datetime(end)
                self.m_model.to_date_filter(my_date, start_time, end_time)
                self.view.draw(self.m_model.df, self.m_model.current_df, self.m_model.image)

            elif command == '/area':
                x1 = input("enter x value for top left point")
                y1 = input("enter y value for top left point")
                x2 = input("enter x value for bottom right point")
                y2 = input("enter y value for bottom right point")
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
            elif command == '/clear':
                self.m_model.clear()

            else:
                print("imvalid command")

            command = input("enter command:")
        print("goodbye")