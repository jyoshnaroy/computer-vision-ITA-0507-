import cv2
import numpy as np
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))
img = np.ones((height, width, 3), dtype=np.uint8) * 255
box_h = height // 10
box_w = width // 10
cv2.rectangle(img, (0, 0), (box_w, box_h), (0, 0, 0), -1)
cv2.rectangle(img, (width-box_w, 0), (width, box_h), (255, 0, 0), -1)
cv2.rectangle(img, (0, height-box_h), (box_w, height), (0, 255, 0), -1)
cv2.rectangle(img, (width-box_w, height-box_h), (width, height), (0, 0, 255), -1)
cv2.imshow("Colored Corners Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
