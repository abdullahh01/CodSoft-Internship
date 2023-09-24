import cv2
import numpy as np

# Load the Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture from the default camera (0)
video_cap = cv2.VideoCapture(0)

while True:
    ret, video_data = video_cap.read()  # Correct variable name 'video_data'

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Create a green background image of the same size as the frame
    green_background = np.zeros_like(video_data)
    green_background[:, :] = (0, 255, 0)  # Set the background color to green

    # Overlay the detected faces on the green background
    for (x, y, w, h) in faces:
        face_roi = video_data[y:y+h, x:x+w]  # Extract the face region
        green_background[y:y+h, x:x+w] = face_roi  # Overlay the face on the green background

    # Display the live video with green background and detected faces
    cv2.imshow("video_live", green_background)

    # Check for the 'a' key press to exit the loop
    if cv2.waitKey(10) == ord("a"):
        break

# Release the video capture object and close all OpenCV windows
video_cap.release()
cv2.destroyAllWindows()
