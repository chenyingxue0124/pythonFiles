import numpy as np
import cv2 as c
import glob
import os

neiborhood8 = np.array([[1, 1, 1],
                        [1, 1, 1],
                            [1, 1, 1]],
                       np.uint8)

path=os.path.expanduser("/Users/chingeisetsu/Desktop/001.png")
img = c.imread(path, 0)
img_dilate = c.dilate(img, neiborhood8, iterations=1)
img_diff = c.absdiff(img, img_dilate)
img_diff_not = c.bitwise_not(img_diff)
img_diff_threshold = c.adaptiveThreshold(img_diff_not,255,c.ADAPTIVE_THRESH_MEAN_C,c.THRESH_BINARY,11,2)


#
#gray = c.cvtColor(img_diff_not, c.COLOR_RGB2GRAY)

c.imwrite(os.path.expanduser("/Users/chingeisetsu/Desktop/001_new.png"), img_diff_threshold)

c.imshow('test',img)
c.imshow('test2',img_dilate)
c.imshow('test3',img_diff)
c.imshow('test4',img_diff_not)
c.imshow('test5',img_diff_threshold)
c.waitKey(10000)

c.destroyAllWindows()