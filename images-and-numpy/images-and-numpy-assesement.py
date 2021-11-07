import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Create a 5 x 5 array of 10's
arr = np.ones((5, 5))
arr * 10

# Populate 5 x 5 array with random integers
np.random.seed(101)
arr = np.random.randint(low=0, high=100, size=(5,5))

# Return largest and smallest values in array
arr.max()
arr.min()

# Open picture of puppy from file path
pic = Image.open('./DATA/00-puppy.jpg')

# Change to numpy array
arr = np.asarray(pic)

# Show the shape of arr which is (1300, 1950, 3)
arr.shape

# Make a copy of the multi-dimensional array that contains the puppy image
mycopy = arr.copy()

# Set the red and green channels to zero
mycopy[:,:,0] = 0
mycopy[:,:,1] = 0

# Show the blue channel
plt.imshow(mycopy) 