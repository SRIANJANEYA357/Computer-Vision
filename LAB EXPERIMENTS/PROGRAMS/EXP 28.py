import cv2

# Input
video = cv2.VideoCapture(r"C:\Users\anji3\Downloads\188613-883402208.mp4")

if not video.isOpened():
    print("Error: Video not found.")
    exit()

background = cv2.createBackgroundSubtractorMOG2()

# Process
while True:
    ret, frame = video.read()

    if not ret:
        break

    mask = background.apply(frame)

    _, threshold = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        threshold,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Vehicle",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Output
    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()