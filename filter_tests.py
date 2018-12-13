import unittest
import pandas as pd
from model import model
class FiltersTestCase(unittest.TestCase):

    def setUp(self):
        self.test_df = pd.read_pickle("data/to_pickle_test_fill.pk1.xz")
        self.model = model("data/to_pickle_test_fill.pk1.xz", "C:\EXELLENTIM\paths0.png")

    ############################test ones filter########################################


    def test_area_filter(self):
        x1 = '0'
        y1 = '0'
        x2 = "5"
        y2 = "150"

        self.model.area_filter((x1, y1), (x2, y2))
        self.assertEqual(1, len(self.model.current_df))

    def test_squers_filter(self):

        x = [20,90]

        self.model.filter_Square(x)
        self.assertEqual(11, len(self.model.current_df))

    def test_date_filter(self):

                my_date = pd.to_datetime("2017-08-17")
                start_time = pd.to_datetime("01:27:10")
                end_time = pd.to_datetime("01:28:18")

                self.model.to_date_filter(my_date, start_time, end_time)
                self.assertEqual(15, len(self.model.current_df))

    def test_time_filter(self):

        start_time = pd.to_datetime("01:27:09")
        end_time = pd.to_datetime("01:28:17")
        self.model.to_time_filter(start_time, end_time)
        self.assertEqual(6, len(self.model.current_df))

    ############################test combination tow filters########################################

    def test_time_filter_and_date_filter(self):

        start_time = pd.to_datetime("01:27:09")
        end_time = pd.to_datetime("01:28:18")
        self.model.to_time_filter(start_time, end_time)

        my_date = pd.to_datetime("2017-08-17")
        start_time = pd.to_datetime("01:28:18")
        end_time = pd.to_datetime("01:29:18")

        self.model.to_date_filter(my_date, start_time, end_time)

        self.assertEqual(9, len(self.model.current_df))

    def test_time_filter_and_squers_filter(self):
        #time_filter
        start_time = pd.to_datetime("01:27:09")
        end_time = pd.to_datetime("01:28:18")
        self.model.to_time_filter(start_time, end_time)

        #squers_filter

        x = [20, 90]
        self.model.filter_Square(x)
        self.assertEqual(10, len(self.model.current_df))

    def test_time_filter_and_area_filter(self):
        #time_filter
        start_time = pd.to_datetime("01:27:09")
        end_time = pd.to_datetime("01:28:18")
        self.model.to_time_filter(start_time, end_time)

        #area_filter
        x1 = "75"
        y1 = "99"
        x2 = "639"
        y2 = "350"

        self.model.area_filter((x1, y1), (x2, y2))
        self.assertEqual(5, len(self.model.current_df))

    def test_date_filter_and_squers_filter(self):

        #date_filter
        my_date = pd.to_datetime("2017-08-17")
        start_time = pd.to_datetime("01:27:10")
        end_time = pd.to_datetime("01:28:18")

        self.model.to_date_filter(my_date, start_time, end_time)

        #squers_filter
        x = [20, 90]
        self.model.filter_Square(x)

        self.assertEqual(10, len(self.model.current_df))

    def test_date_filter_and_test_area_filter(self):
        # date_filter
        my_date = pd.to_datetime("2017-08-17")
        start_time = pd.to_datetime("01:27:10")
        end_time = pd.to_datetime("01:28:18")

        self.model.to_date_filter(my_date, start_time, end_time)

        #test_area_filter
        x1 = "75"
        y1 = "99"
        x2 = "639"
        y2 = "350"

        self.model.area_filter((x1, y1), (x2, y2))
        self.assertEqual(5, len(self.model.current_df))

    def test_squers_filter_and_test_area_filter(self):

        #squers_filter

        x = [20, 90]

        self.model.filter_Square(x)

        x1 = "75"
        y1 = "99"
        x2 = "639"
        y2 = "350"

        #area_filter

        self.model.area_filter((x1, y1), (x2, y2))
        self.assertEqual(0, len(self.model.current_df))

    def test_clear(self):

        len_table_before_filter = len(self.model.current_df)
        start_time = pd.to_datetime("01:27:09")
        end_time = pd.to_datetime("01:28:18")

        self.model.to_time_filter(start_time, end_time)
        self.model.clear()

        self.assertEqual(len_table_before_filter, len(self.model.current_df))


if __name__ == '__main__':
    unittest.main()