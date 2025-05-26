import random
from tkinter import ttk
import tkinter as tk
from tkinter import * 
from tkinter.ttk import Button, Label, Frame
from tkinter import PhotoImage
from PIL import Image, ImageTk

master = Tk()
master.geometry("700x700")
master.title("Rock, Paper, Scissors, Lizard, Spock")
image = ImageTk.PhotoImage(Image.open("rpsls.png"))
master.configure(background='#171515')



style = ttk.Style()
style.theme_use('clam')
style.configure("Custom.TButton",
                foreground="white",
                background="#171515")

style2 = ttk.Style()
style2.theme_use('clam')
style2.configure("Custom.TFrame",
                background="#171515",)
                
computer_value = { 
 "0": "Rock",
 "1": "Paper",
 "2": "Scissors",
 "3": "Lizard",
 "4": "Spock"
}

def ifrock():
 c = computer_value[str(random.randint(0, 4))]
 if c == "Rock":
  result = "Draw"
 elif c == "Scissors":
  result = "Player Wins"
 elif c == "Lizard":
  result = "Player Wins"
 elif c == "Spock":
  result = "Computer Wins"
 else:
  result = "Computer Wins"
 l4.config(text=result)
 l1.config(text="Rock   ")
 l3.config(text=c)

def ifpaper():
 c = computer_value[str(random.randint(0, 4))]
 if c == "Paper":
  result = "Draw"
 elif c == "Scissors":
  result = "Computer Wins"
 elif c == "Lizard":
  result = "Computer Wins"
 elif c == "Spock":
  result = "Player Wins"
 else:
  result = "Player Wins"
 l4.config(text=result)
 l1.config(text="Paper   ")
 l3.config(text=c)

def ifscissors():
 c = computer_value[str(random.randint(0, 4))]
 if c == "Rock":
  result = "Computer Wins"
 elif c == "Scissors":
   result = "Draw"
 elif c == "Lizard":
   result = "Player Wins"
 elif c == "Spock":
  result = "Computer Wins"
 else:
  result = "Player Wins"
 l4.config(text=result)
 l1.config(text="Scissors   ")
 l3.config(text=c)    
 
def iflizard():
 c = computer_value[str(random.randint(0, 4))]
 if c == "Rock":
  result = "Computer Wins"
 elif c == "Scissors":
   result = "Computer Wins"
 elif c == "Lizard":
   result = "Draw"
 elif c == "Spock":
  result = "Player Wins"
 else:
  result = "Player Wins"
 l4.config(text=result)
 l1.config(text="Lizard   ")
 l3.config(text=c)  
 
def ifspock():
 c = computer_value[str(random.randint(0, 4))]
 if c == "Rock":
  result = "Player Wins"
 elif c == "Scissors":
   result = "Player Wins"
 elif c == "Lizard":
   result = "Computer Wins"
 elif c == "Spock":
  result = "Draw"
 else:
  result = "Computer Wins"
 l4.config(text=result)
 l1.config(text="Spock   ")
 l3.config(text=c)     

ttk.Label(master,
 text="Rock Paper Scissors Lizard Spock",
 style="Custom.TButton").pack(pady=20)

frame = ttk.Frame(master,
 style="Custom.TButton")
frame.pack()

l1 = Label(frame,
  text="Player",
 style="Custom.TButton")

l2 = Label(frame,
  text="           VS",
 style="Custom.TButton")

l3 = Label(frame, text="Computer",
 style="Custom.TButton")

image = Image.open('rpsls.png')
image = ImageTk.PhotoImage(image)

il = tk.Label(master, image=image)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()


l4 = Label(master,
  text="",
  width=15,
  borderwidth=2,
  relief="solid",
 style="Custom.TButton")
l4.pack(pady=20)

frame1 = Frame(master,
 style="Custom.TFrame")
frame1.pack()

b1 = Button(frame1, text="🪨", width=7,
   command=ifrock,
   style="Custom.TButton")

b2 = Button(frame1, text="📄", width=7,
   command=ifpaper,
   style="Custom.TButton")

b3 = Button(frame1, text="✂️", width=7,
   command=ifscissors,
   style="Custom.TButton")

b4 = Button(frame1, text="🦎", width=7,
   command=iflizard,
   style="Custom.TButton")

b5 = Button(frame1, text="🖖", width=7,
   command=ifspock,
   style="Custom.TButton")

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(side=LEFT, padx=10)
b4.pack(side=LEFT, padx=10)
b5.pack(padx=10)

il.pack(pady=50)

master.resizable(True, True)
master.mainloop()