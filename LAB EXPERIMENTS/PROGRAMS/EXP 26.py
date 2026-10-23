import cv2

# Input
video = cv2.VideoCapture(r"C:\Users\anji3\Downloads\188613-883402208.mp4")

if not video.isOpened():
    print("Error: Video not found.")
    exit()

frames = []

# Process
while True:
    ret, frame = video.read()

    if not ret:
        break

    frames.append(frame)

video.release()

# Output
for frame in reversed(frames):
    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()