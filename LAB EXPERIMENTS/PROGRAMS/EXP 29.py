import cv2
import urllib.request
import os

# Input
image = cv2.imread(r"C:\Users\anji3\Downloads\happy-group-boys-outside-24998397.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

face_model = "haarcascade_frontalface_default.xml"
eye_model = "haarcascade_eye.xml"

# Download models automatically
if not os.path.exists(face_model):
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/opencv/opencv/4.x/data/haarcascades/haarcascade_frontalface_default.xml",
        face_model
    )

if not os.path.exists(eye_model):
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/opencv/opencv/4.x/data/haarcascades/haarcascade_eye.xml",
        eye_model
    )

face_cascade = cv2.CascadeClassifier(face_model)
eye_cascade = cv2.CascadeClassifier(eye_model)

# Process
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

for (x, y, w, h) in faces:

    face_gray = gray[y:y+h, x:x+w]
    face_color = image[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(
        face_gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(
            face_color,
            (ex, ey),
            (ex + ew, ey + eh),
            (0, 255, 0),
            2
        )

# Output
cv2.imshow("Eye Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()