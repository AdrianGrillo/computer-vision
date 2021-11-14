import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Top left corner of rectangle: // operator so that output is an integer and not a float 
x = width // 2
y = height // 2

# Width and height of rectangle
w = width // 4
h = height // 4

while True: 
    ret, frame = cap.read()
    
    # Draw the rectangle
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 4)

    # Show the video capture only after drawing the rectangle
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()