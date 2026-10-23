import cv2

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

# Process
watermark = image.copy()

cv2.putText(
    watermark,
    "WATERMARK",
    (50, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    2,
    (215, 225, 244),
    3
)

# Output
cv2.imshow("Original Image", image)
cv2.imshow("Watermarked Image", watermark)

cv2.waitKey(0)
cv2.destroyAllWindows()