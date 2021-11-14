import cv2 

# Callback function to draw rectangle
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, topLeft_clicked, botRight_clicked
    
    if event == cv2.EVENT_LBUTTONDOWN: 
        # Reset all global variables after drawing rectangle
        if topLeft_clicked and botRight_clicked:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topLeft_clicked = False
            botRight_clicked = False
            
        if topLeft_clicked == False: 
            pt1 = (x, y)
            topLeft_clicked = True
            
        elif botRight_clicked == False:
            pt2 = (x, y)
            botRight_clicked = True

# Global variables
pt1 = (0, 0)
pt2 = (0, 0)
topLeft_clicked = False
botRight_clicked = False

# Connect to callback
cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)


while True: 
    ret, frame = cap.read()
    
    # Drawing on frame based on global variables
    if topLeft_clicked:
        cv2.circle(frame, pt1, 3, (0, 0, 255), -1)
        
    # If pt1 and pt2 have been updated with new x, y values then draw the rectangle with those values
    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 3)
    
    cv2.imshow('Test', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()