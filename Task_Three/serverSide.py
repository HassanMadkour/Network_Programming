from socket import *
import threading
import tkinter as tk
from tkinter import messagebox


player = 2
turn = 1


def win(player):
    messagebox.showinfo(title="Congratulation",
                        message='winner is ' + player)
    window.destroy()


def check():
    global turn
    turn += 1

    b1 = btn1['text']
    b2 = btn2['text']
    b3 = btn3['text']
    b4 = btn4['text']
    b5 = btn5['text']
    b6 = btn6['text']
    b7 = btn7['text']
    b8 = btn8['text']
    b9 = btn9['text']

    if (b1 == b2 and b2 == b3 and b1 == 'O') or (b1 == b2 and b2 == b3 and b1 == 'X'):
        win(b1)
    if (b4 == b5 and b5 == b6 and b4 == 'O') or (b4 == b5 and b5 == b6 and b4 == 'X'):
        win(b4)
    if (b7 == b8 and b8 == b9 and b7 == 'O') or (b7 == b8 and b8 == b9 and b7 == 'X'):
        win(b7)
    if (b1 == b4 and b4 == b7 and b1 == 'O') or (b1 == b4 and b4 == b7 and b1 == 'X'):
        win(b1)
    if (b2 == b5 and b5 == b8 and b2 == 'O') or (b2 == b5 and b5 == b8 and b2 == 'X'):
        win(b2)
    if (b3 == b6 and b6 == b9 and b3 == 'O') or (b3 == b6 and b6 == b9 and b3 == 'X'):
        win(b3)
    if (b1 == b5 and b5 == b9 and b1 == 'O') or (b1 == b5 and b5 == b9 and b1 == 'X'):
        win(b1)
    if (b3 == b5 and b5 == b7 and b3 == 'O') or (b3 == b5 and b5 == b7 and b3 == 'X'):
        win(b3)


def click1():
    global player
    if btn1["text"] == " ":
        if player == 2:
            player = 1
            btn1["text"] = "O"
            send(1)
        check()


def click2():
    global player
    if btn2["text"] == " ":
        if player == 2:
            player = 1
            btn2["text"] = "O"
            send(2)
        check()


def click3():
    global player
    if btn3["text"] == " ":
        if player == 2:
            player = 1
            btn3["text"] = "O"
            send(3)

        check()


def click4():
    global player
    if btn4["text"] == " ":
        if player == 2:
            player = 1
            btn4["text"] = "O"
            send(4)

        check()


def click5():
    global player
    if btn5["text"] == " ":
        if player == 2:
            player = 1
            btn5["text"] = "O"
            send(5)
        check()


def click6():
    global player
    if btn6["text"] == " ":
        if player == 2:
            player = 1
            btn6["text"] = "O"
            send(6)
        check()


def click7():
    global player
    if btn7["text"] == " ":
        if player == 2:
            player = 1
            btn7["text"] = "O"
            send(7)
        check()


def click8():
    global player
    if btn8["text"] == " ":
        if player == 2:
            player = 1
            btn8["text"] = "O"
            send(8)
        check()


def click9():
    global player
    if btn9["text"] == " ":
        if player == 2:
            player = 1
            btn9["text"] = "O"
            send(9)
        check()


def click11():
    for btn in button_list:
        btn["text"] = " "
    global player
    player = 2
    send(11)


def receive():
    while True:
        num_button = session.recv(10)
        num_button = int(num_button)
        global player

        if num_button == 11:
            for btn in button_list:
                btn["text"] = " "
        else:
            button_list[num_button - 1]["text"] = "X"
        player = 2


def send(mess):
    mess = str(mess)
    session.send(mess.encode())


s = socket(AF_INET, SOCK_STREAM)
s.bind(("127.0.0.1", 1123))
s.listen(5)
session, add = s.accept()
window = tk.Tk()
window.title('Client: tic tac toe')
window.geometry('260x130')
lb1 = tk.Label(window, text='player1: O', font=('Helvetica', '15'))
lb1.grid(row=0, column=0)
btn1 = tk.Button(master=window, text=" ", bg='White',
                 fg='black', width=3, command=click1)
btn1.grid(row=1, column=1)
btn2 = tk.Button(master=window, text=" ", bg='White',
                 fg='black', width=3, command=click2)
btn2.grid(row=1, column=2)
btn3 = tk.Button(master=window, text=" ", bg='White',
                 fg='black', width=3, command=click3)
btn3.grid(row=1, column=3)
btn4 = tk.Button(master=window, text=" ", bg='White',
                 fg='black', width=3, command=click4)
btn4.grid(row=2, column=1)
btn5 = tk.Button(master=window, text=" ", bg='White',
                 fg='black', width=3, command=click5)
btn5.grid(row=2, column=2)
btn6 = tk.Button(master=window, text=" ", bg='White',
                 fg='black', width=3, command=click6)
btn6.grid(row=2, column=3)
btn7 = tk.Button(master=window, text=" ", bg='White',
                 fg='black', width=3, command=click7)
btn7.grid(row=3, column=1)
btn8 = tk.Button(master=window, text=" ", bg='White',
                 fg='black', width=3, command=click8)
btn8.grid(row=3, column=2)
btn9 = tk.Button(master=window, text=" ", bg='White',
                 fg='black', width=3, command=click9)
btn9.grid(row=3, column=3)

btn11 = tk.Button(master=window, text="Reset", bg='White',
                  fg='black', width=3, command=click11)
btn11.grid(row=4, column=3)
button_list = list()
button_list.append(btn1)
button_list.append(btn2)
button_list.append(btn3)
button_list.append(btn4)
button_list.append(btn5)
button_list.append(btn6)
button_list.append(btn7)
button_list.append(btn8)
button_list.append(btn9)

threading.Thread(target=receive).start()
tk.mainloop()
