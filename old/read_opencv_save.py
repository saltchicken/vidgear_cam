import cv2

# Open the camera (0 is typically the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera is opened correctly
if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()

# height, width = 320, 240
height, width = 540, 960

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # Set width to 640 pixels
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height) # Set height to 480 pixels
cap.set(cv2.CAP_PROP_FPS, 30.0)
print(cv2.CAP_PROP_FPS)



# Define the codec and create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec (XVID is widely supported)
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (width, height))  # Output file, FPS, resolution

while True:
    # Capture frame-by-frame
    print(cap.get(cv2.CAP_PROP_FPS))
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Write the frame to the output video file
    out.write(frame)
    print('saving frame')



# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()

