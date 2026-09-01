import cv2
img = cv2.imread("image.jpg")
text = input("Enter text: ")
cv2.putText(img, text, (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2)

cv2.imshow("Image with Text", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
