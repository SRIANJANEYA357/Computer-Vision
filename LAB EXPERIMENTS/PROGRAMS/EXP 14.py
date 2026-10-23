import cv2
import numpy as np

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

# Process
height, width = image.shape[:2]

src = np.float32([
    [0, 0],
    [width - 1, 0],
    [0, height - 1],
    [width - 1, height - 1]
])

dst = np.float32([
    [50, 50],
    [width - 50, 0],
    [0, height - 50],
    [width, height]
])

matrix = cv2.getPerspectiveTransform(src, dst)

result = cv2.warpPerspective(image, matrix, (width, height))

# Output
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()