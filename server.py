import cv2
from vidgear.gears import NetGear

# Initialize OpenCV video capture (use 0 for the default camera)
cap = cv2.VideoCapture(0)  # Replace 0 with your camera index or video file path

# Configure NetGear server
server = NetGear(address="10.0.0.2", port="5555", protocol="tcp", logging=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # OpenCV processing (e.g., converting to grayscale)
   # processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Send the processed frame to the client
    server.send(frame)

    

# Release resources
cap.release()
server.close()
cv2.destroyAllWindows()
