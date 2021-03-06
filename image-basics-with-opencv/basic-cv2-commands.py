import numpy as np
import matplotlib.pyplot as plt
import cv2

# Read an image with cv2, this is preferable to Image.open() because the image is brought in as a numpy array by default
img = cv2.imread('../DATA/00-puppy.jpg')

# By default, cv2 color channel orientation is BGR so if we display an image with matplotlib, the red and blue colors will be switched. That's because matplotlib expects images to be in RGB format. 

# Convert from BGR to RGB 
fixed_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# If working with other color mappings, cv2 also has available the functionality to convert to HSL and HSV

# Bring in an image in grayscale (No color channels)
img_grey = cv2.imread('../DATA/00-puppy.jpg', cv2.IMREAD_GREYSCALE)

# imread uses a default color mapping so if img_grey is passed to imread then it won't be in grayscale. To remedy this, pass cmap='gray' and now the image will be shown in grayscale. 

# Output the grayscale image using gray color mapping 
plt.imshow(img_grey, cmap='gray')

# Resize images with a width of 1000px and a height of 400px
new_img = cv2.resize(fixed_img, (1000, 400))

# Resize images with ratios 

w_ratio = 0.5
h_ratio = 0.5
resized_img = cv2.resize(fixed_img, (0,0), fixed_img, w_ratio, h_ratio)

#After resizing fixed_img by a factor of 50%, the shapes of each image are as follows:
fixed_img.shape = (1950, 1300, 3)
resized_img.shape = (650, 975, 3)

# Flip an image on the x-axis
flipped_img = cv2.flip(fixed_img, 0)

# Flip an image on the y-axis
flipped_img = cv2.flip(fixed_img, 1)

# Flip an image on the x-axis and y-axis
flipped_img = cv2.flip(fixed_img, -1)

# Adjust the amount of canvas space allowed an image in jupyter notebook by adjusting the integers in figsize
fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(111)
ax.imshow(fixed_img)