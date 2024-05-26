import json
from os import system
import random
from customtkinter import *
from time import sleep



currency = "€"
"""
if bet_amount > money:
		print("u broke")
		continue
	if bet_amount<500:
		print("i cant be lower than 500")
		continue
	if bet_color not in betcolors:
		print("that color in not on the table")
		continue
"""

money = 20000
betcolors = ["red","black","green"]

while True:
	bet_color = input("Which color? ")
	bet_amount = input("How much do you bet? ")

	results = [None,bet_amount]
	
	if bet_amount.isdigit():
		bet_amount = int(bet_amount)
	else:
		print("Amount not a digit!")
		continue
	if bet_amount > money:
		print("You dont have enough money! in other words you're broke.")
		continue
	if bet_amount<500:
		print(f"Minimum is 500 {currency}!")
		continue
	if bet_color not in betcolors:
		print("That color doesn't exist!")
		continue
	
	

	if (random.random() < 0.02) and (bet_color == "green"):
		print("You win!")
		money = bet_amount * 12
		print(f"You have {money} {currency}")
		continue
	elif (random.random() > 0.02) and (bet_color == "green"):
		print(f"You lost {bet_amount * 12} {currency}, winner was {random.choice(['red', 'black'])}")
		money -= bet_amount * 12
		print(f"You have {money} {currency}")
		continue
	if (random.random() < 0.49) and (bet_color == "black" or bet_color == "red"):
		rand = random.randint(0,1)
		if rand == 0:
			results[0] = "red"
		elif rand == 1:
			results[0] = "black"
		if results[0] == bet_color:
			print("You win!")
			money += bet_amount * 2
			print(f"You have {money} {currency}")
			continue
		else:
			print(f"You lose, winner was {results[0]}")
			money -= bet_amount * 2
			print(f"You have {money} {currency}")
	else:
		rand2 = random.randint(0,1)
		if rand2 == 0:
			results[0] = "red"
		elif rand2 == 1:
			results[0] = "black"
		if results[0] == bet_color:
			print("You win!")
			money += bet_amount * 2
			print(f"You have {money} {currency}")
			continue
		else:
			print(f"You lose, winner was {results[0]}")
			money -= bet_amount * 2
			print(f"You have {money} {currency}")

# set_default_color_theme("dark-blue")
# set_appearance_mode("Dark")
# root = CTk()
# root.title("PyGamble")
# moneylabel = Label(root, text=f"You have: {money} {currency}.")
# combobox = CTkComboBox(root, values=options)
# combobox.pack()
# root.mainloop()
