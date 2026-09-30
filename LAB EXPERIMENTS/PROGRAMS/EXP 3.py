import cv2

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

# Check image
if image is None:
    print("Error: Image not found.")
    exit()

# Process
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 100, 200)

# Output
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()