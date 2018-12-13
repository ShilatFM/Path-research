from controller import controller
# if __name__ == '__main__':
#    # p_path = input("enter picture path: ")
#    # im = imread(p_path)
#    #
#    # df_path = input("enter data path: ")
#    # df = pd.read_pickle(df_path)

df_path = "data/to_pickle.pk1.xz"
p_path = "data/paths0.png"
print("im here")
c = controller(df_path, p_path)
c.run()
# TODO LIST:

#PICKLE FILE
#view
#cli


# input validation
# input for squers