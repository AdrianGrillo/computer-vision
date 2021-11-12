import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
pic = Image.open('DATA/00-puppy.jpg')
pic_arr = np.asarray(pic)

plt.imshow(pic_arr)

# This results in an image being displayed

pic_arr.shape

# (1300, 1950, 3) 3 images to makeup one, each image contains only red, blue, in green varying in different amounts.
# Use array slicing to manipulate a certain color channel and zero our certain indexes to remove color from certain spots in the image
