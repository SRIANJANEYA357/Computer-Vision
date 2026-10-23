import cv2
import numpy as np

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

# Process
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5, 5), np.uint8)

black_hat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

# Output
cv2.imshow("Original Image", image)
cv2.imshow("Black Hat Image", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()