import cv2

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

# Process
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Output
cv2.imshow("Original Image", image)
cv2.imshow("Gray-scale Image", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()