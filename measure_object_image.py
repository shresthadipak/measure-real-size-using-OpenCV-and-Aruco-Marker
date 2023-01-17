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
    cv2.polylines(img, [cnt], True, (0, 0, 255), 2)

    # draw rect
    rect = cv2.minAreaRect(cnt)
    (x,y), (w, h), angle =  rect

    cv2.circle(img, (int(x), int(y)), 5, (255, 0, 0), -1)

    box = np.int0(cv2.boxPoints(rect))

    print(box)

cv2.imshow("Measure Object Size", img)

cv2.waitKey(0) 
cv2.destroyAllWindows()