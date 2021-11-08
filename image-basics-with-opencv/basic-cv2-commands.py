import numpy as np
import matplotlib.pyplot as plt
import cv2

# Read an image with cv2, this is preferable to Image.open() because the image is brought in as a numpy array by default
img = cv2.imread('../DATA/00-puppy.jpg')

# By default, cv2 color channel orientation is BGR so if we display an image with matplotlib, the red and blue colors will be switched. That's because matplotlib expects images to be in RGB format. 

# Convert from BGR to RGB 
fixed_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Bring in an image in grayscale (No color channels)
img_grey = cv2.imread('../DATA/00-puppy.jpg', cv2.IMREAD_GREYSCALE)

# imread uses a default color mapping so if img_grey is passed to imread then it won't be in grayscale. To remedy this, pass cmap='gray' and now the image will be shown in grayscale. 

plt.imshow(img_grey, cmap='gray')