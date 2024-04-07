# -*- coding: utf-8 -*-
"""
@author: ChatRoom ==> Client
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 30300))


def send_function():
    message = input("user1 : ")
    # send length of message first
    s.send(len(message).to_bytes(4, byteorder='big'))
    # then send the message
    s.send(message.encode())


def receive_function():
    msg_length = s.recv(4)  # Receive from the connection socket
    msg_length = int.from_bytes(msg_length, byteorder='big')

    received_message = s.recv(msg_length)  # Receive from the connection socket
    print(received_message.decode())


try:
    while True:
        send_function()
        receive_function()
except KeyboardInterrupt:
    print("chat terminated")
    s.close()
