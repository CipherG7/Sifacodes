import cv2

# Load the pre-trained Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the default webcam
webcam = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not webcam.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Read a frame from the webcam
    ret, frame = webcam.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Error: Failed to capture image")
        break

    # Convert the frame to grayscale (Haar cascade works with grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with the detected faces
    cv2.imshow('Face Detection', frame)

    # Break the loop if the user presses 'q'
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# Release the webcam and close the window
webcam.release()
cv2.destroyAllWindows()
