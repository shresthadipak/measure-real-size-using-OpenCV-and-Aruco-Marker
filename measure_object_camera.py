import cv2
from objectDetector import objDetector
import numpy as np

# call object
detector = objDetector()

# Load aruco detector
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    if not ret:
        break

    # Get Aruco marker
    corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

    # Draw polygon around the marker
    int_corners = np.int0(corners)
    cv2.polylines(img, int_corners, True, (0, 0, 255), 5)

    if corners:
        #Aruco Perimeter
        aruco_perimeter = cv2.arcLength(corners[0], True)

        # Pixel to cm ratio
        pixel_cm_ratio = aruco_perimeter / 20
    else:
        pixel_cm_ratio = 29.526773834228514


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

        # Get Width and Height of the Objects by applying the Ratio pixel to cm
        object_width = w / pixel_cm_ratio
        object_height = h / pixel_cm_ratio

        #display an image size 
        cv2.putText(img, f'Width: {round(object_width, 1)} cm', (int(x), int(y)-50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
        cv2.putText(img, f'Height: {round(object_height, 1)} cm', (int(x), int(y)-30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)

    cv2.imshow("Measure Object Size", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()