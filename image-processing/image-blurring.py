import cv2
import numpy as np 
import matplotlib.pyplot

img = cv2.imread('../DATA/bricks.jpg').astype(np.float32) / 255
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Import an image and place text across it to make blurring more obvious
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text='tight pussy', org=(10, 600), fontFace=font, fontScale=10, color=(255, 0, 0), thickness=4)

# Define kernel
kernel = np.ones(shape=(5,5), dtype=np.float32) / 25

# Apply kernel to image for blurring. -1 indicates that the output depth will be the same as the input depth. 
dst = cv2.filter2D(img, -1, kernel)

# Blur image with cv2's predefined kernel values 
blurred = cv2.blur(img, ksize=(5, 5))

# Gaussian blur: Takes values from multiple pixels in a square and spits out one pixel with the averaged values 
blurred_img = cv2.GaussianBlur(img, (5, 5), 10)

# Median blur: Works the same way as gaussian blur with the intension of reducing noise while maintaining sharpness
median = cv2.medianBlur(img, 5)

# Honorable mention: Bilateral blurring which is also intended to reduce noise while maintaining a sharp image but this comes at a cost as it is quite slow. 