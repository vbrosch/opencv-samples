"""
    Implementation of the official opencv tutorial. Available at:
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
"""

import cv2 as cv

video_path = 'sample_files/Panasonic_HDC_TM_700_P_50i.avi'

cap = cv.VideoCapture(video_path)

fourcc = int(cap.get(cv.CAP_PROP_FOURCC))

print("fourcc is ", fourcc)

# Define the codec and create VideoWriter object
out = cv.VideoWriter('sample_files/output.avi', fourcc, 25.0, (1920, 1080))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv.flip(frame, 0)

        # write the flipped frame
        out.write(frame)

        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
