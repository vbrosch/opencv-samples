import cv2 as cv

b = 0


def set_b(x):
    global b
    b = x


img_path = "sample_files/lena.png"
img_path_2 = "sample_files/opencv_logo.png"

img1 = cv.imread(img_path)
img2 = cv.imread(img_path_2)

cv.namedWindow('image')
cv.createTrackbar('Overlay', 'image', 0, 100, set_b)


while True:
    img_res = cv.addWeighted(img1, (1 - (b / 100.0)), img2, (b / 100.0), 0)
    cv.imshow('image', img_res)

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
