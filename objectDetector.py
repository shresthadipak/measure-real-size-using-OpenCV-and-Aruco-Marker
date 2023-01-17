import cv2

class objDetector():

    def __init__(self):
        pass


    def detect_object(self, image):

        # convert image into grayscale
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Create a mask with adaptive threshold
        mask = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 5)

        # find contuors
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        object_contours = []

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area > 1000:
                object_contours.append(cnt)

        # print(object_contours)    

        return object_contours
