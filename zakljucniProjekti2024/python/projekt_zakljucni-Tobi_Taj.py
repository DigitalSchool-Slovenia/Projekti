from tkinter import *

root = Tk()



def check():
	global victory
	if btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X':
		victory_lbl.config(text='Victory!')
		victory = True



	elif btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X':
		victory_lbl.config(text='Victory!')
		victory = True


	elif btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X':
		victory_lbl.config(text='Victory!')
		victory = True




	elif btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X':
		victory_lbl.config(text='Victory!')
		victory = True


	elif btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X':
		victory_lbl.config(text='Victory!')
		victory = True


	elif btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X':
		victory_lbl.config(text='Victory!')
		victory = True

	elif btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X':
		victory_lbl.config(text='Victory!')
		victory = True


	elif btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X':
		victory_lbl.config(text='Victory!')
		victory = True


	else:
 		print('no victory yet...')


	if victory:
		btn1['text'] = ' '
		btn2['text'] = ' '
		btn3['text'] = ' '
		btn4['text'] = ' '
		btn5['text'] = ' '
		btn6['text'] = ' '
		btn7['text'] = ' '
		btn8['text'] = ' '
		btn9['text'] = ' '

victory = False


#mytxt = button.cget() ---> get text from button
root.geometry('500x400')
root.title('OFFICE NINJAS: križci in krožci')
root.resizable(False, False)


crcorx = 'X'
player1turn = True

victory_lbl = Label(root, text='', fg='Green', font=('Arial', 40))
victory_lbl.place(x=300, y=200)



def Click1():
	global player1turn
	if player1turn:
		btn1.config(text=crcorx)
		player1turn = False

	else:
		btn1.config(text='O')
		player1turn = True



	check()


def Click2():
	global player1turn
	if player1turn:
		btn2.config(text=crcorx)
		player1turn = False

	else:
		btn2.config(text='O')
		player1turn = True


	check()

def Click3():
	global player1turn
	if player1turn:
		btn3.config(text=crcorx)
		player1turn = False

	else:
		btn3.config(text='O')
		player1turn = True


	check()



def Click4():
	global player1turn
	if player1turn:
		btn4.config(text=crcorx)
		player1turn = False

	else:
		btn4.config(text='O')
		player1turn = True


	check()


def Click5():
	global player1turn
	if player1turn:
		btn5.config(text=crcorx)
		player1turn = False

	else:
		btn5.config(text='O')
		player1turn = True


	check()


def Click6():
	global player1turn
	if player1turn:
		btn6.config(text=crcorx)
		player1turn = False

	else:
		btn6.config(text='O')
		player1turn = True


	check()


def Click7():
	global player1turn
	if player1turn:
		btn7.config(text=crcorx)
		player1turn = False

	else:
		btn7.config(text='O')
		player1turn = True


	check()


def Click8():
	global player1turn
	if player1turn:
		btn8.config(text=crcorx)
		player1turn = False

	else:
		btn8.config(text='O')
		player1turn = True


	check()

def Click9():
	global player1turn
	if player1turn:
		btn9.config(text=crcorx)
		player1turn = False

	else:
		btn9.config(text='O')
		player1turn = True


	check()


btn1 = Button(root, text=' ', font=('Arial', 40), command=Click1) 
btn2 = Button(root, text=' ', font=('Arial', 40), command=Click2) 
btn3 = Button(root, text=' ', font=('Arial', 40), command=Click3) 

btn4 = Button(root, text=' ', font=('Arial', 40), command=Click4) 
btn5 = Button(root, text=' ', font=('Arial', 40), command=Click5) 
btn6 = Button(root, text=' ', font=('Arial', 40), command=Click6) 

btn7 = Button(root, text=' ', font=('Arial', 40), command=Click7) 
btn8 = Button(root, text=' ', font=('Arial', 40), command=Click8) 
btn9 = Button(root, text=' ', font=('Arial', 40), command=Click9)


btn1.place(x=10, y=10)
btn2.place(x=100, y=10)
btn3.place(x=200, y=10)

btn4.place(x=10, y=120)
btn5.place(x=100, y=120)
btn6.place(x=200, y=120)

btn7.place(x=10, y=230)
btn8.place(x=100, y=230)
btn9.place(x=200, y=230)

root.mainloop()