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