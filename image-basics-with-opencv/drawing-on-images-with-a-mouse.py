import cv2
import numpy as np

# Variables

drawing = False
ix, iy = -1, -1

# Function

def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0, 255, 0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (255, 0, 0), -1)

def draw_rectangle(event, x, y, flags, param):

    # Continuously track the values of these 3 global variables
    global drawing, ix, iy 

    if event == cv2.EVENT_LMOUSEBUTTONDOWN: 
        drawing = True
        # Set ix and iy equal to the position of the cursor when the left mouse button is pressed initially 
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE: 
        cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), -1)
    elif event == cv2.EVENT_LMOUSEBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), -1)


# Show Image

img = np.zeros((512, 512, 3), np.int32)

# Name the window then connect that window by name to the functions defined as draw_circle and draw_rectangle
cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', draw_circle)
cv2.setMouseCallback('my_drawing', draw_rectangle)

while True: 
    cv2.imshow('my_drawing', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
