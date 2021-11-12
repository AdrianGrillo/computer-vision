import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
    blank_img =np.zeros((600,600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img,text='ABCDE',org=(50,300), fontFace=font,fontScale= 5,color=(255,255,255),thickness=25,lineType=cv2.LINE_AA)
    return blank_img

def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

img = load_img()

# Erosion: Used to blur the bounderies between the background and the foreground. To increase the effect, increment the number of iterations. 
kernel = np.ones((5, 5), np.uint8)
result = cv2.erode(img, kernel, iterations=4)

# Opening: Erosion followed by dilation, this can be helpful when trying to remove noise from the background of an image. 

# Add noise to the background
white_noise = np.random.randint(0, 2, (600, 600))
white_noise = white_noise * 255
noise_img = white_noise + img

# Remove noise from the background 
opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernel)

# Closing: Used to eliminate noise from the foreground, inverse operation to opening. 
closing = cv2.morphologyEx(black_noise_img, cv2.MORPH_CLOSE, kernel)

# Morphological Gradient: Takes the difference between dilation and erosion of an image and essentially just grabs the edgees. Can be used as a crude form of edge detection. 
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
