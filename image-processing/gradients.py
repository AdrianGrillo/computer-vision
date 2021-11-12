import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

img = cv2.imread('../DATA/sudoku.jpg', 0)

# Sobel gradient for x derivative: This will show vertical edges and fade horizontal ones
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, 5)

# Sobel for y does the inverse
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, 5)

# Blend them for a clearer representation of each 
blended_sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Laplacian attempts to do both at once 
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Combining multiple morphological operators can improve a programs edge detection depending the programs specific use case and purpose. 
kernel = np.ones((4,4), np.uint8)
gradient = cv2.morphologyEx(blended_sobel, cv2.MORPH_GRADIENT, kernel)