import pickle
import socket
import struct
from cv2 import cv2

IP_address = '127.0.0.1'
PORT = 5678

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((IP_address, PORT))
server.listen()
print('Waiting for users to join the call...')

conn, addr = server.accept()

data = b'' 
payload_size = struct.calcsize("L")

while True:

    # Retrieve message size
    while len(data) < payload_size:
        data += conn.recv(4096)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0] ### CHANGED

    # Retrieve all data based on message size
    while len(data) < msg_size:
        data += conn.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Extract frame
    frame = pickle.loads(frame_data)

    # Display
    cv2.imshow('videocall in progress...', frame)
    cv2.waitKey(1)