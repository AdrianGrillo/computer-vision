import cv2
import time

# By providing a file path instead of 0 to VideoCapture, all frames returned are from the designated video at the file path
cap = cv2.VideoCapture('mysupervideo.mp4')

# Check if cap is opened to ensure we passed a valid file path and codec to the write object
if cap.usOpened() == False:
    print('ERROR: INVALID FILE PATH OR CODEC')

# Display video data from file 
while True: 
    ret, frame = cap.read()

    if ret == True:
        # For viewing purposes, the video should be shown back at the same speed it was recorded in which was 30 FPS. 
        # So show only 1 frame per 1/30th of a second to return the original playback speed. 
        time.sleep(1/30) 
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    # If ret == false then no more frames are being returned from cap.read() therefore the video is finished so close the window
    else: 
        break

cap.release()
cv2.destroyAllWindows()