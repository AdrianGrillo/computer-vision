import cv2

# Start reading video data from default camera device
cap = cv2.VideoCapture(0)

# Get the width and height of the video data being returned from capture and convert it from a floating point to integer
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create writer object. String passed to second param is OS dependent, since I'm on windows it DIVX. 
<<<<<<< HEAD
writer = cv2.VideoWriter('mysupervideo.mp4', cv2.VideoWriter_fourcc(*'mpv4'), 30, (width, height))
=======
writer = cv2.VideoWriter('mysupervideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))
>>>>>>> a5f8898928d6a19d2c608f145c274ab920e7fbe6

# Write and display video capture data
while True: 
    ret, frame = cap.read()

    # Any sort of operations to be performed to the capture data (like drawing on it or object detection) would go here before it's written or displayed 
    writer.write(frame)
    cv2.imshow(frame, frame)
    
    # If the user presses q, then break out of the while loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture and write object then close the window that's displaying the video capture data
cap.release()
writer.release()
cv2.destroyAllWindows()
