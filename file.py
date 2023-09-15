import random
from tkinter import *


def checkwinner():

    for row in range(3):

        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):

        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif not emptyspace():

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    else:
        return False


def newgame():

    global player

    player = random.choice(players)

    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#FFFBFC")


def next(row, column):
    global player

    if buttons[row][column]['text'] == "" and checkwinner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            buttons[row][column]['font'] = ("consolas", 10)
            if checkwinner() is False:
                player = players[1]
                label.config(text=players[1] + " turn")

            elif checkwinner() is True:
                label.config(text=players[0] + " won")
            elif checkwinner() == "tie":
                label.config(text="tie")

        else:
            buttons[row][column]['text'] = player
            buttons[row][column]['font'] = ("consolas", 10)
            if checkwinner() is False:
                player = players[0]
                label.config(text=players[0] + " turn")
            elif checkwinner() is True:
                label.config(text=players[1] + " won")
            elif checkwinner() == "tie":
                label.config(text="tie")


def emptyspace():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


window = Tk()
window.title("tic tac toe")

players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(window, text=player + " turn", font=("consolas", 40))
label.pack(side=TOP)

frame = Frame(window)
frame.pack()

reset_button = Button(text="RESET", height=2, width=8, command=newgame, font=('Ariel,40'))
reset_button.pack(side=BOTTOM)

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, bg="white", height=8, width=20,font=("consolas",10),
                                      command=lambda row=row, column=column: next(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()


