"""
    Draw the ~~ opencv logo using opencv (it's not perfect, but it illustrates the basic idea)
"""

import cv2 as cv
import numpy as np

img = np.ones((512, 512, 3), np.uint8) * 255

# draw the o
img = cv.ellipse(img, (256, 128), (100, 100), 135, 0, 270, (0, 0, 255), -1)
img = cv.circle(img, (256, 128), 35, (255, 255, 255), -1)

# draw the c
img = cv.ellipse(img, (128, 512-200), (100, 100), 25, 0, 270, (0, 255, 0), -1)
img = cv.circle(img, (128, 512-200), 35, (255, 255, 255), -1)

# draw the v
img = cv.ellipse(img, (512-128, 512-200), (100, 100), 360-45, 0, 270, (255, 0, 0), -1)
img = cv.circle(img, (512-128, 512-200), 35, (255, 255, 255), -1)

# text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10, 500), font, 4, (0, 0, 0), 2, cv.LINE_AA)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()


