import cv2

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

# Process
rotated_image = cv2.rotate(image, cv2.ROTATE_180)

# Output
cv2.imshow("Original Image", image)
cv2.imshow("180 Degree Rotated Image", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()