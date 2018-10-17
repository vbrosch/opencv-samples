"""
    Implementation of the official opencv tutorial. Available at:
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_trackbar/py_trackbar.html
"""

import cv2 as cv
import numpy as np

r, g, b, s = 0, 0, 0, 0


def set_r(x):
    global r
    r = x


def set_g(x):
    global g
    g = x


def set_b(x):
    global b
    b = x


def set_s(x):
    global s
    s = x


# create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

# trackbars
cv.createTrackbar('R', 'image', 0, 255, set_r)
cv.createTrackbar('G', 'image', 0, 255, set_g)
cv.createTrackbar('B', 'image', 0, 255, set_b)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, set_s)

while True:
    cv.imshow('image', img)
    k = cv.waitKey(1)

    if k == ord('q'):
        break

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()