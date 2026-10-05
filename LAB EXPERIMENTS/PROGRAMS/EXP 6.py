import cv2
import numpy as np

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

# Check image
if image is None:
    print("Error: Image not found.")
    exit()

# Process
kernel = np.ones((5, 5), np.uint8)
eroded_image = cv2.erode(image, kernel, iterations=1)

# Output
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()