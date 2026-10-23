import cv2

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

# Process
x1, y1 = 50, 50
x2, y2 = 200, 200

cropped = image[y1:y2, x1:x2]

copy = cropped.copy()

h, w = copy.shape[:2]

image[250:250+h, 250:250+w] = copy

# Output
cv2.imshow("Original and Pasted Image", image)
cv2.imshow("Cropped ROI", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()