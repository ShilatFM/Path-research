import matplotlib.pyplot as plt

class view:

    def __init__(self):
       pass

    def draw(self, original_df, current_df, img):

        print("im in draw")
        table = current_df.groupby(['filename', 'obj']).size()
        df_by_obj = original_df.set_index(['filename', 'obj']).sort_index()

        plt.imshow(img)


        for t in table.index:
            s_o = df_by_obj.loc[t]
            plt.plot(s_o.x, s_o.y, label = t[1])
        plt.legend(loc=9, bbox_to_anchor=(1.1, 1))

        plt.show()