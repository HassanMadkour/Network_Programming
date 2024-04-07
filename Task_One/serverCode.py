# -*- coding: latin-1 -*-
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 3000))
s.listen(10)
c, add = s.accept()


def send_function():
    message = input("your mess : ")
    c.send(len(message).to_bytes(4, byteorder='big'))
    c.send(message.encode())


def receive_function():
    msg_length = s.recv(4)
    msg_length = int.from_bytes(msg_length, byteorder='big')

    received_message = c.recv(msg_length)
    print(received_message.decode())


try:
    while True:
        send_function()
        receive_function()
except KeyboardInterrupt:
    c.close()
    s.close()
