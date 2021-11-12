import cv2
import numpy as np
import matplotlib.pyplot as plt

# Different variables are set for BGR and RGB images as to calculate the histogram values for each image, cv2 expects the color channels to be in BGR but for showing purposes, RGB is necessary to relate the values in the histogram for how the image actually looks. 
dark_horse = cv2.imread('../DATA/horse.jpg')
show_horse = cv2.cvtColor(dark_horse, cv2.COLOR_BGR2RGB)

rainbow = cv2.imread('../DATA/rainbow.jpg')
show_rainbow =cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)

blue_bricks = cv2.imread('../DATA/bricks.jpg')
show_bricks = cv2.cvtColor(blue_bricks, cv2.COLOR_BGR2RGB)

# Calculate histogram values for dark_horse image for the blue channel with no mask, a max value of 255 and with a range of 0-255
hist_values = cv2.calcHist([dark_horse], [0], None, [256], [0, 256])

# Calculate histogram values for each color channel on the blue_bricks image and plot them together
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([blue_bricks], [i], None, [256], [0, 256])
    plt.plot(histr, col)
    plt.xlim([0, 256])
    
plt.title('HISTOGRAM FOR BLUE BRICKS')

###################################################
## Display the histogram of an image with a mask ##
###################################################
img = rainbow

# img.shape = (550, 413, 3)
# Create a black canvas with the same shape as img 
mask = np.zeros(img.shape[:2], np.uint8)

# Set a portion of the black image to white, this is the area where the original image will shine through while everything else remains black
mask[300:400, 100:400] = 255

# Place the mask over the image 
masked_img = cv2.bitwise_and(img,img, mask=mask)

# Calulate the histogram for the masked image, then plot them
hist_masked_values_red = cv2.calcHist([rainbow], channels=[2], mask=mask, histSize=[256], ranges=[0, 256])
plt.plot(hist_masked_values_red)

##########################################
## Equalize a Grayscale and Color Image ##
##########################################

gorilla = cv2.imread('../DATA/gorilla.jpg', 0)

def display_img(img,cmap=None):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)

# Equalize the greyscale image 
eq_gorilla = cv2.equalizeHist(gorilla)

# To equalize a color image, the format must be HSV, so convert HSV
color_gorilla = cv2.imread('../DATA/gorilla.jpg')
hsv = cv2.cvtColor(color_gorilla, cv2.COLOR_BGR2HSV)

# Equalize only the value channel of the HSV image then reset the value chanel to the new equalized values
hsv[:,:,2] = cv2.equalizeHist(hsv[:,:,2]) 