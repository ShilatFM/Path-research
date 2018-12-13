import pandas as pd

def creat():
    df = pd.read_pickle("data/to_pickle.pk1.xz")
    df = df.head(20)
    df.to_pickle('data/to_pickle_test_fill.pk1.xz')
    test_df = pd.read_pickle("data/to_pickle_test_fill.pk1.xz")
creat()