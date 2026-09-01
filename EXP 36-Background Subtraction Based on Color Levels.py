import cv2
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold_value = 100     
_, result = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_TOZERO)
cv2.imshow("Original Image", img)
cv2.imshow("Background Subtracted Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
