import cv2
import numpy as np 
import matplotlib.pyplot as plt

# Full image: This will be searched
full = cv2.imread('../DATA/sammy.jpg')
full = cv2.cvtColor(full, cv2.COLOR_BGR2RGB)

# Smaller image: This will be slid across full image to find match
face = cv2.imread('../DATA/sammy_face.jpg')
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

# Different template matching methods
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# This for loop will go through each of the methods and use template matching with that method

for m in methods:
    
    # Create a copy of the image since a rectngle will be drawn around the match
    full_copy = full.copy()
    
    # Evaluate the list of strings as cv2 functions
    method = eval(m)
    
    # Template matching
    res = cv2.matchTemplate(full_copy, face, method)
    
    # Deriving values to draw rectangle with
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # Since SQDIFF finds template with min values, if the method is SQDIFF, the image template begins at min values instead of max
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc # (x, y)
    else: 
        # Top left value is the beginning value where cv2.matchTemplate is most certain of an image match
        top_left = max_loc
        
    height, width, cannels = face.shape
    
    # (x value of top left + the width of the small image, y value of top_left + height of small image)
    # NOTE: Since matplotlib starts image at 0 from top left, height is added from top left and this traverses the rectangle DOWN the plot
    bottom_right = (top_left[0] + width, top_left[1] + height)
    
    # Draw rectangle
    cv2.rectangle(full_copy, top_left, bottom_right, (255, 0, 0), 10)
    
    # Plot and show images 
    plt.subplot(121)
    plt.imshow(res)
    plt.title('Heat map of template matching')
    
    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title('Detection of template')
    
    # Title both plots with method used
    plt.suptitle(m)
    
    # Don't erase the plots afte each iteration of the loop
    plt.show()
    
    print('\n')
    print('\n')