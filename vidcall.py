from cv2 import cv2
import socket
import pickle
import struct


video = cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('',5678))

while(True):
    ret, image = video.read()
    data = pickle.dumps(image)
    message_size = struct.pack("L", len(data))
    clientsocket.sendall(message_size + data)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

