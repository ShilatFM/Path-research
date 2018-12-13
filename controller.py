import seaborn
import matplotlib.pyplot as plt
from model import model
from view import view
import pandas as pd
CONST_SQUERS = 10
class controller:

    def __init__(self, df_path, p_path):
        self.m_model = model(df_path, p_path)
        self.view = view()

    def run(self):
        com = self.view.run(self.m_model.image, self.m_model.df, self.m_model.current_df)

        while(com[0] != "end"):
            if com[0] == "clear":
                self.m_model.clear()

            elif com[0] == "area":
                self.m_model.area_filter(com[1], com[2])

            elif com[0] == "time":
                if len(com) == 3:
                    self.m_model.to_time_filter(com[1], com[2])

            elif com[0] == "date":
                if len(com) == 4:
                    self.m_model.to_date_filter(com[1], com[2], com[3])

            elif com[0] == "area_squers":
                self.m_model.filter_Square(com[1])

            elif com[0] == "draw_one_by_one":
                self.view.draw_one_by_one(self.m_model.df, self.m_model.current_df, self.m_model.image)

            elif com[0] == "draw":
                self.view.draw(self.m_model.df, self.m_model.current_df, self.m_model.image)

            elif com[0] == "heatmap":
                   seaborn.heatmap(self.m_model.df)
                   plt.show()

            com = self.view.run(self.m_model.image, self.m_model.df, self.m_model.current_df)

