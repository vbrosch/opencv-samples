"""
    Implementation of the official opencv tutorial. Available at:
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
"""

import cv2 as cv
import matplotlib.pyplot as plt

img_path = "sample_files/lena.png"
img_path_grayscale = "sample_files/lena_gray.png"
use_matplot_viewer = True

# load an color assigned image
img = cv.imread(img_path)

# convert to gray scale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

if not use_matplot_viewer:
    cv.imshow(img_path, img)
    cv.imshow(img_path_grayscale, img_gray)

    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

cv.imwrite(img_path_grayscale, img_gray)

