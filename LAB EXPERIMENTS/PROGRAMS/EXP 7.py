import cv2

# Input
video = cv2.VideoCapture(r"C:\Users\anji3\Downloads\188613-883402208.mp4")

if not video.isOpened():
    print("Error: Video not found.")
    exit()

# Process
while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    key = cv2.waitKey(30) & 0xFF

    if key == ord('s'):
        cv2.waitKey(100)

    elif key == ord('f'):
        video.grab()

    elif key == ord('q'):
        break

# Output
video.release()
cv2.destroyAllWindows()