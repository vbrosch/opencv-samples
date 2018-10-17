"""
    Implementation of the paint exercise in the official opencv tutorial. Available at:
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_trackbar/py_trackbar.html
"""

import cv2 as cv
import numpy as np

r, g, b = 255, 255, 255
drawing = False
mode = True
ix, iy = -1, -1


def set_r(x):
    global r
    r = x


def set_g(x):
    global g
    g = x


def set_b(x):
    global b
    b = x


def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
            else:
                cv.circle(img, (x, y), 5, (b, g, r), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
        else:
            cv.circle(img, (x, y), 5, (b, g, r), -1)


# create a black image, a window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw)

# trackbars
cv.createTrackbar('R', 'image', 255, 255, set_r)
cv.createTrackbar('G', 'image', 255, 255, set_g)
cv.createTrackbar('B', 'image', 255, 255, set_b)

while True:
    cv.imshow('image', img)
    k = cv.waitKey(1)

    if k == ord('q'):
        break
    if k == ord('m'):
        mode = not mode

cv.destroyAllWindows()
