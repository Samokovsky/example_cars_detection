import cv2
from modules.detector import CarsDetection

cd = CarsDetection()
img = cd.detect_car(cv2.imread("images/test1.jpg"))

cv2.imshow("Cars", img)
cv2.waitKey(0)