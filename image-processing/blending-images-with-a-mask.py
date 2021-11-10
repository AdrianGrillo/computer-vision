import cv2
import numpy as np
import matplotlib.pyplot as plt

# Import images to be overlaid and resize accordingly
img1 = cv2.imread('../DATA/dog_backpack.png')
img2 = cv2.imread('../DATA/watermark_no_copy.png')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img2 = cv2.resize(img2, (600, 600))

rows, cols, channels = img2.shape

# Define the Region of Interest

# Subtract the width of the smaller image from the width of the larger
x_offset = img1.shape[1] - cols

# Subtract the height of the smaller image from the height of the larger
y_offset = img1.shape[0] - rows

#Now x_offset and y_offset correspond to where we want our Region of Interest or ROI to begin

# The ROI begins at the y and x offset and ends at the bottom right corner of img1
roi = img1[y_offset:1401, x_offset:934]

# Convert image to be overlaid to grayscale 
img2gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

# Invert values so that the background is black as only the white areas will pass through the mask
mask_inv = cv2.bitwise_not(img2gray)

# Create a a multidimensional array in the shape of img2 and fill all indices with 8bit integer values of 255
# white_background will have three color channels of only white, this is what our mask will be overlaid onto
white_background = np.full(img2.shape, 255, dtype=np.uint8)

# Take white_background and place mask_inv over it on all three color channels
bk = cv2.bitwise_or(white_background, white_background, mask=mask_inv)

# Take the original img2 and for all three color channels, place mask_inv on top of it
# Now the red from the original image will show and the black background of mask_inv covers everything else 
foreground = cv2.bitwise_or(img2, img2, mask=mask_inv)

# Finally, take the original roi of the large_img and place foreground over it
final_roi = cv2.bitwise_or(roi, foreground)

# The final step is to overlay that new ROI over the original large_img using numpy indexing 
large_img = img1
small_img = final_roi

large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img

# Now, if plt.imshow(large_img) is invoked, only the colored portion of small_img is overlayed on top of it and nothing else