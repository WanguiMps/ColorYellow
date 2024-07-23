import cv2
import numpy as np
from util import get_limits

yellow = (0, 255, 255)  # Yellow in BGR color space

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame.")
        break
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerlimit, upperlimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImage, lowerlimit, upperlimit)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Assuming you want the bounding box of the largest contour
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        
        # Draw the bounding box
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Detected 'q' key press. Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
