import cv2

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

# Check image
if image is None:
    print("Error: Image not found.")
    exit()

# Process
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Output
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blurred Image", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()