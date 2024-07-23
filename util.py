import numpy as np
import cv2

def get_limits(color):
    """
    Given a BGR color, convert it to HSV and return the lower and upper limits for color detection.
    """
    # Convert the BGR color to a 1x1 pixel image
    color_pixel = np.uint8([[color]])
    
    # Convert the BGR color to HSV
    hsv_color = cv2.cvtColor(color_pixel, cv2.COLOR_BGR2HSV)[0][0]
    
    # Define lower and upper limits with some tolerance
    lower_limit = np.array([hsv_color[0] - 10, 100, 100], dtype=np.uint8)
    upper_limit = np.array([hsv_color[0] + 10, 255, 255], dtype=np.uint8)
    
    return lower_limit, upper_limit
