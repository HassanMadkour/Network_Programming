# client server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 3000))


def send_function():
    message = input("your mess : ")
    # i send len of message first
    s.send(len(message).to_bytes(4, byteorder='big'))
    # then send the mess
    s.send(message.encode())


def receive_function():
    msg_length = s.recv(4)
    msg_length = int.from_bytes(msg_length, byteorder='big')

    received_message = s.recv(msg_length)
    print(received_message.decode())


try:
    while True:
        send_function()
        receive_function()
except KeyboardInterrupt:
    s.close()
