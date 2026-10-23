from builtins import exit

import cv2
import numpy as np

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

# Process
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.cornerHarris(gray, 2, 3, 0.04)

image[corners > 0.01 * corners.max()] = [0, 0, 255]

# Output
cv2.imshow("Harris Corner Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()