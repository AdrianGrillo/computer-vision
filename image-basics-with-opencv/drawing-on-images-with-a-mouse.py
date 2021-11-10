import cv2
import numpy as np

# Function

def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0, 255, 0), -1)

# Name the window then connect that window by name to the function defined as draw_circle
cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', draw_circle)


# Show Image

img = np.zeros((512, 512, 3), np.int32)

while True: 
    cv2.imshow('my_drawing', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
