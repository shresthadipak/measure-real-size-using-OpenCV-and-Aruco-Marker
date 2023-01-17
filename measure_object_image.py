import cv2
from objectDetector import objDetector
import numpy as np

# call object
detector = objDetector()

# import image data and read it
image_path = 'images/image2.jpg'
img = cv2.imread(image_path)

# Load Object detector module
contours = detector.detect_object(img)

for cnt in contours:
    # Draw polygon
    # cv2.polylines(img, [cnt], True, (0, 0, 255), 2)

    # draw rect
    rect = cv2.minAreaRect(cnt)
    (x,y), (w, h), angle =  rect

    box = np.int0(cv2.boxPoints(rect))

    # display the center point in an object
    cv2.circle(img, (int(x), int(y)), 5, (255, 0, 0), -1)

    # draw a rectangle box in objects
    cv2.polylines(img, [box], True, (0, 255, 0), 2)

    # display an image size 
    cv2.putText(img, f'Width: {round(w, 1)}', (int(x), int(y)-50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
    cv2.putText(img, f'Height: {round(h, 1)}', (int(x), int(y)-30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

cv2.imshow("Measure Object Size", img)

cv2.waitKey(0) 
cv2.destroyAllWindows()