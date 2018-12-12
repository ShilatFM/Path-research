import pylab
import matplotlib.image as plt
import pandas as pd
def function_4(list_test, num_segmentation ):
    im = plt.imread("C:\EXELLENTIM\paths0.png")
    locaition = []
    im_size = im.shape
    width = im_size[1]
    height = im_size[0]
    for i in list_test:
        r = i // num_segmentation
        c = i - (r * num_segmentation)
        locaition.append((((c + 1) * width / num_segmentation, r * height / num_segmentation),
                          (c * width / num_segmentation, (r + 1) * height / num_segmentation)))
    return locaition
def test_function_4():
    list_test = [1, 6, 8]
    num_segmentation = 3
    print([((426.6666666666667, 0.0), (213.33333333333334, 120.0)),
     ((213.33333333333334, 240.0), (0.0, 360.0)),
     ((640.0, 240.0), (426.6666666666667, 360.0))]
     == function_4(list_test, num_segmentation))

test_function_4()