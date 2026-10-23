import cv2

# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")
template = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\watch.png")

if image is None or template is None:
    print("Error: Image or template not found.")
    exit()

# Process
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(
    gray_image,
    gray_template,
    cv2.TM_CCOEFF_NORMED
)

_, max_value, _, max_location = cv2.minMaxLoc(result)

h, w = gray_template.shape

if max_value > 0.4:
    x, y = max_location

    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.putText(
        image,
        "Object Detected",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )
else:
    cv2.putText(
        image,
        "Object Not Detected",
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

# Output
cv2.imshow("Object Recognition", image)

cv2.waitKey(0)
cv2.destroyAllWindows()