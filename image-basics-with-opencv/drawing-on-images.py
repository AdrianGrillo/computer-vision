import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a 512 x 512 blank canvas of 16 bit integers
blank_img = cv2.zeros(shape=(512, 512), dtype=np.int16)

# Draw a rectangle on the blank_img with the top left vertice at (384,10) and the bottom right vertice at (500,150)
cv2.rectangle(blank_img, pt1=(384,10), pt2=(500,150), color=(255,0,0), thickness=5)

# Draw a circle on blank_img with a center at (100, 100), a radius of 50, with the color filled in
cv2.circle(blank_img, (100,100), 50, color=(0,255,255), thickness=-1)

# Draw a line from the top left of the image to the bottom right
cv2.line(blank_img, pt1=(0,512), pt2=(512,0), color=(0,0,255), thickness=10)

# Define tuples that each correspond to a point of a polygon
vertices = np.array([ [100,300], [200,200], [400,300], [200,400] ], dtype=np.int32)

# Reshape to be in the format that cv2 expects
points = vertices.reshape(-1,1,2)

# Draw the polygon onto blank_img. Note: point values must be passed in an array
cv2.polylines(blank_img, [points], isClosed=True, color=(255,0,0), thickness=5)