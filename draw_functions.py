"""
    Implementation off the official opencv tutorial. Available at:
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html
"""

import numpy as np
import cv2 as cv

# black image
img = np.zeros((512, 512, 3), np.uint8)

# diagonal blue line
img = cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# draw rectangle
img = cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# draw circle
img = cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
# draw an ellipse
img = cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv.polylines(img, [pts], True, (0, 255, 255))

# text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()