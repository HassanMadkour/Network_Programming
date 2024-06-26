# -*- coding: utf-8 -*-
"""
@author: ChatRoom ==> Server
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 30300))
s.listen()
c, add = s.accept()


def send_function():
    message = input("user2: ")
    c.send(len(message).to_bytes(4, byteorder='big'))
    c.send(message.encode())


def receive_function():
    msg_length = c.recv(4)  # Receive from the connection socket
    msg_length = int.from_bytes(msg_length, byteorder='big')

    received_message = c.recv(msg_length)  # Receive from the connection socket
    print(received_message.decode())


try:
    while True:
        receive_function()
        send_function()
except KeyboardInterrupt:
    print("chat terminated")
    c.close()
    s.close()
