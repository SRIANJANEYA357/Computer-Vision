import cv2
import numpy as np

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

# Process
rows, cols = image.shape[:2]

points1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

points2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

matrix = cv2.getAffineTransform(points1, points2)

transformed_image = cv2.warpAffine(
    image,
    matrix,
    (cols, rows)
)

# Output
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", transformed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()