import cv2
import matplotlib.pyplot as plt

# Import the image as grayscale so it can be converted to binary with one less step
img = cv2.imread('../DATA/rainbow.jpg', 0)

# ret is assigned the value at which the threshold is set and binary is set to the actual thresholded image
# For binary specifically, all values < 127 will be set to 0 and all values > 127 will be set to the max value passed to it (255)
ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Import new image that will be used for adaptive thresholding
img2 = cv2.imread('../DATA/crossword.jpg', 0)

# Show image as a bigger figure in jupyter notebook
def show_pic(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img, 'gray')

# Add binary threshold to second image 
ret, th1 = cv2.threshold(img2, 180, 255, cv2.THRESH_BINARY)

# With the binary threshold, some parts of the image are too dark leaving the text blurry and illegible, this will be remedied with an adaptive threshold
th2 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 15)

# Due to the neighborhood we set of 5 pixels, the dark areas of the crossword puzzle aren't blacked out even though the text is readable now. Since each image comes with pros and cons, let's blend them to create something better than either alone
blended = cv2.addWeighted(th1, 0.6, th2, 0.4, 0)