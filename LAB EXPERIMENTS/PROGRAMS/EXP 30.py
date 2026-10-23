import cv2
import urllib.request
import os

# Input
image = cv2.imread(r"C:\Users\anji3\Downloads\images.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

face_model = "haarcascade_frontalface_default.xml"
smile_model = "haarcascade_smile.xml"

if not os.path.exists(face_model):
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/opencv/opencv/4.x/data/haarcascades/haarcascade_frontalface_default.xml",
        face_model
    )

if not os.path.exists(smile_model):
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/opencv/opencv/4.x/data/haarcascades/haarcascade_smile.xml",
        smile_model
    )

face_cascade = cv2.CascadeClassifier(face_model)
smile_cascade = cv2.CascadeClassifier(smile_model)

# Process
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(40, 40)
)

for (x, y, w, h) in faces:

    face_gray = gray[y:y+h, x:x+w]
    face_color = image[y:y+h, x:x+w]

    mouth_start = int(h * 0.5)

    mouth_gray = face_gray[mouth_start:h, :]

    smiles = smile_cascade.detectMultiScale(
        mouth_gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(20, 20)
    )

    for (sx, sy, sw, sh) in smiles:

        sy = sy + mouth_start

        cv2.rectangle(
            face_color,
            (sx, sy),
            (sx + sw, sy + sh),
            (0, 255, 0),
            2
        )

        cv2.putText(
            face_color,
            "Smile",
            (sx, sy - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

# Output
cv2.imshow("Smile Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()