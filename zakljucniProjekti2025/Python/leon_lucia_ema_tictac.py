from tkinter import *

player1 = True
player2 = False
game = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def check():
    global game
    if (game[0] == 1 and game[1] == 1 and game[2] == 1):
        label.config(text = "Player1 wins!")
    if (game[3] == 1 and game[4] == 1 and game[5] == 1):
        label.config(text = "Player1 wins!")
    if (game[6] == 1 and game[7] == 1 and game[8] == 1):
        label.config(text = "Player1 wins!")
    if (game[0] == 1 and game[3] == 1 and game[6] == 1):
        label.config(text = "Player1 wins!")
    if (game[1] == 1 and game[4] == 1 and game[7] == 1):
        label.config(text = "Player1 wins!")
    if (game[2] == 1 and game[5] == 1 and game[8] == 1):
        label.config(text = "Player1 wins!")
    if (game[0] == 1 and game[4] == 1 and game[8] == 1):
        label.config(text = "Player1 wins!")
    if (game[2] == 1 and game[4] == 1 and game[6] == 1):
        label.config(text = "Player1 wins!")

    if (game[0] == 2 and game[1] == 2 and game[2] == 2):
        label.config(text = "Player2 wins!")
    if (game[3] == 2 and game[4] == 2 and game[5] == 2):
        label.config(text = "Player2 wins!")
    if (game[6] == 2 and game[7] == 2 and game[8] == 2):
        label.config(text = "Player2 wins!")
    if (game[0] == 2 and game[3] == 2 and game[6] == 2):
        label.config(text = "Player2 wins!")
    if (game[1] == 2 and game[4] == 2 and game[7] == 2):
        label.config(text = "Player2 wins!")
    if (game[2] == 2 and game[5] == 2 and game[8] == 2):
        label.config(text = "Player2 wins!")
    if (game[0] == 2 and game[4] == 2 and game[8] == 2):
        label.config(text = "Player2 wins!")
    if (game[2] == 2 and game[4] == 2 and game[6] == 2):
        label.config(text = "Player2 wins!")

def press(number):
    global player1, player2, game
    if (player1 == True):
            if(number == 1):
                b1.config(text = "X")
                game[0] = 1
            if(number == 2):
                b2.config(text = "X")
                game[1] = 1
            if(number == 3):
                b3.config(text = "X")
                game[2] = 1
            if(number == 4):
                b4.config(text = "X")
                game[3] = 1
            if(number == 5):
                b5.config(text = "X")
                game[4] = 1
            if(number == 6):
                b6.config(text = "X")
                game[5] = 1
            if(number == 7):
                b7.config(text = "X")
                game[6] = 1
            if(number == 8):
                b8.config(text = "X")
                game[7] = 1
            if(number == 9):
                b9.config(text = "X")
                game[8] = 1

    if (player2 == True):
            if(number == 1):
                b1.config(text = "O")
                game[0] = 2
            if(number == 2):
                b2.config(text = "O")
                game[1] = 2
            if(number == 3):
                b3.config(text = "O")
                game[2] = 2
            if(number == 4):
                b4.config(text = "O")
                game[3] = 2
            if(number == 5):
                b5.config(text = "O")
                game[4] = 2
            if(number == 6):
                b6.config(text = "O")
                game[5] = 2
            if(number == 7):
                b7.config(text = "O")
                game[6] = 2
            if(number == 8):
                b8.config(text = "O")
                game[7] = 2
            if(number == 9):
                b9.config(text = "O")
                game[8] = 2
    player1 = not player1
    player2 = not player2
    check()

master = Tk()
master.geometry("950x900")
#canvas = Canvas(master, width=800, height=600)
master.config(background='#3eedf4')

b1 = Button(master, text=" ", command=lambda: press(1), height=3, width=7, font=('Helvetica', 50))
b2 = Button(master, text=" ", command=lambda: press(2), height=3, width=7, font=('Helvetica', 50))
b3 = Button(master, text=" ", command=lambda: press(3), height=3, width=7, font=('Helvetica', 50))
b4 = Button(master, text=" ", command=lambda: press(4), height=3, width=7, font=('Helvetica', 50))
b5 = Button(master, text=" ", command=lambda: press(5), height=3, width=7, font=('Helvetica', 50))
b6 = Button(master, text=" ", command=lambda: press(6), height=3, width=7, font=('Helvetica', 50))
b7 = Button(master, text=" ", command=lambda: press(7), height=3, width=7, font=('Helvetica', 50))
b8 = Button(master, text=" ", command=lambda: press(8), height=3, width=7, font=('Helvetica', 50))
b9 = Button(master, text=" ", command=lambda: press(9), height=3, width=7, font=('Helvetica', 50))


b1.grid(row=1, column=0, sticky=W, pady=2)
b2.grid(row=2, column=0, sticky=W, pady=2)
b3.grid(row=3, column=0, sticky=W, pady=2)
b4.grid(row=1, column=1, sticky=W, pady=2)
b5.grid(row=2, column=1, sticky=W, pady=2)
b6.grid(row=3, column=1, sticky=W, pady=2)
b7.grid(row=1, column=2, sticky=W, pady=2)
b8.grid(row=2, column=2, sticky=W, pady=2)
b9.grid(row=3, column=2, sticky=W, pady=2)

label = Label(master, text="Tic-Tac-Toe", font=('Helvetica', 32), bg="#3eedf4" )





label.grid(row=0, column=0, columnspan=3, pady=10)


mainloop()  