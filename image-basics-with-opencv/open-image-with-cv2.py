import cv2

img = cv2.imread('../DATA/00-puppy.jpg')

while True :
    cv2.imshow('Puppy', img)

    # If we've waited at least one millesecond and pressed the escape key, break out of the while loop
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Then close the window containing the image that's being displayed 
cv2.destroyAllWindows()