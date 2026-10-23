import cv2
import urllib.request
import os

# Input
image = cv2.imread(r"C:\Users\anji3\Downloads\happy-group-boys-outside-24998397.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

model = "face_detection_yunet_2026may.onnx"

if not os.path.exists(model):
    print("Downloading face detection model...")
    url = "https://github.com/opencv/opencv_zoo/raw/refs/heads/main/models/face_detection_yunet/face_detection_yunet_2026may.onnx"
    urllib.request.urlretrieve(url, model)

# Process
height, width = image.shape[:2]

detector = cv2.FaceDetectorYN.create(
    model,
    "",
    (width, height),
    0.3,
    0.3,
    5000
)

_, faces = detector.detect(image)

if faces is not None:
    for face in faces:
        x, y, w, h = face[:4].astype(int)

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

# Output
print("Faces detected:", 0 if faces is None else len(faces))

cv2.imshow("Face Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()