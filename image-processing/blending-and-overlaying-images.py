import cv2
import numpy as np
import matplotlib.pyplot as plt

# Import images and convert them to RGB values
img1 = cv2.imread('../DATA/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread('../DATA/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Resize images to the same dimensions to blend together
img1 = cv2.resize(img1, (1200, 1200))
img2 = cv2.resize(img2, (1200, 1200))

# Blend the two images together with a 9:1 ratio of img1:img2 nad a gamma value of 0
blended_img = cv2.addWeighted(img1, 0.9, img2, 0.1, 0)

# Reimport images to overlay them
# Import images and convert them to RGB values
img1 = cv2.imread('../DATA/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread('../DATA/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2 = cv2.resize(img2, (600, 600))

# Reassign images new names for clarity
large_img = img1
small_img = img2

# x and y values for where small_img will start to be overlayed across large_img
x_offset = 0
y_offset = 0

# By looking at the image shapes, we can see that the first integer corresponds to the height
# large_img.shape = (1401, 934, 3)
# small_img.shape = (600, 600, 3)

x_end = x_offset + small_img.shape[1]
y_end = y_offset + small_img.shape[0]

# Overlay the images with reassignment
large_img[y_offset:y_end, x_offset:x_end] = small_img