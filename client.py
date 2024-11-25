import cv2
import socket
import pickle

# Setup socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 5000))

while True:
    data, _ = sock.recvfrom(65536)
    frame = pickle.loads(data)

    # Display frame
    cv2.imshow('Video Stream', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
sock.close()

