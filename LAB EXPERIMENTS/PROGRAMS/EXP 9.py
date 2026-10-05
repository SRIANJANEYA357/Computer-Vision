import cv2

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

# Check image
if image is None:
    print("Error: Image not found.")
    exit()

# Process
bigger_image = cv2.resize(image, None, fx=2, fy=2)
smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5)

# Output
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger_image)
cv2.imshow("Smaller Image", smaller_image)

cv2.waitKey(0)
cv2.destroyAllWindows()