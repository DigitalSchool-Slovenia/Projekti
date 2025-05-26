from  tkinter import Tk, Frame,  Label, LEFT,  BOTH, Entry, W, E, Button, messagebox, ttk
from tkinter import font as tkFont  # for convenience

global igralec_X 
igralec_X = True
global vsepozicije

root= Tk()
root.geometry("600x600")
root.resizable(0,0)

fontsize = tkFont.Font(family='Arial', size=36)

style=ttk.Style()
style.theme_use("clam")
style.configure("Custom.TButton", padding=(60,60), foreground= "darkgrey", background="lightgrey", font=('Helvetica 70'))

root.columnconfigure(0, weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

vsepozicije=["","","","","","","","",""]

def reset():
    global igralec_X, vsepozicije
    igralec_X=False
    button_1.config(text="")
    button_2.config(text="")
    button_3.config(text="")
    button_4.config(text="")
    button_5.config(text="")
    button_6.config(text="")
    button_7.config(text="")
    button_8.config(text="")
    button_9.config(text="")
    vsepozicije=["","","","","","","","",""]


def checkwin():
    if vsepozicije[0]==vsepozicije[1]== vsepozicije[2] and vsepozicije[1]!="":
        win=messagebox.askyesno("WE HAVE A WINNER!", "Player "+vsepozicije[1]+ " you won!!                             Would you like to play  again?")
        if win==False:
            root.destroy()
        elif win==True:
            reset()
    elif vsepozicije[3]==vsepozicije[4]== vsepozicije[5] and vsepozicije[3]!="":
        win=messagebox.askyesno("WE HAVE A WINNER!", "Player "+vsepozicije[3]+ " you won!!                               Would you like to play  again?")
        if win==False:
            root.destroy()
        elif win==True:
            reset()
    elif vsepozicije[6]==vsepozicije[7]== vsepozicije[8] and vsepozicije[6]!="":
        win=messagebox.askyesno("WE HAVE A WINNER!", "Player "+vsepozicije[6]+ " you won!!                              Would you like to play  again?")
        if win==False:
            root.destroy()
        elif win==True:
            reset()
    elif vsepozicije[0]==vsepozicije[3]== vsepozicije[6] and vsepozicije[0]!="":
        win=messagebox.askyesno("WE HAVE A WINNER!", "Player "+vsepozicije[0]+ " you won!!                             Would you like to play  again?")
        if win==False:
            root.destroy()
        elif win==True:
            reset()
    elif vsepozicije[1]==vsepozicije[4]== vsepozicije[7] and vsepozicije[1]!="":
        win=messagebox.askyesno("WE HAVE A WINNER!", "Player "+vsepozicije[4]+ " you won!!                               Would you like to play  again?")
        if win==False:
            root.destroy()
        elif win==True:
            reset()
    elif vsepozicije[2]==vsepozicije[5]== vsepozicije[8] and vsepozicije[2]!="":
        win=messagebox.askyesno("WE HAVE A WINNER!", "Player "+vsepozicije[7]+ " you won!!                              Would you like to play  again?")
        if win==False:
            root.destroy()
        elif win==True:
            reset()
    elif vsepozicije[0]==vsepozicije[4]== vsepozicije[8] and vsepozicije[8]!="":
        win=messagebox.askyesno("WE HAVE A WINNER!", "Player "+vsepozicije[8]+ " you won!!                               Would you like to play  again?")
        if win==False:
            root.destroy()
        elif win==True:
            reset()
    elif vsepozicije[2]==vsepozicije[4]== vsepozicije[6] and vsepozicije[2]!="":
        win=messagebox.askyesno("WE HAVE A WINNER!", "Player "+vsepozicije[2]+ " you won!!                              Would you like to play  again?")
        if win==False:
            root.destroy()
        elif win==True:
            reset()


def button_1():
    global vsepozicije
    global igralec_X 
    
    if igralec_X == True and vsepozicije[0]=="":
        button_1.config(text="X")
        button_1.update_idletasks()
        vsepozicije[0]="X"
        igralec_X = False
    elif igralec_X == False and vsepozicije[0]=="":
        button_1.config(text="O")
        button_1.update_idletasks()
        vsepozicije[0]="O"
        igralec_X = True
    checkwin()


def button_2():
    global vsepozicije
    global igralec_X
    if igralec_X == True and vsepozicije[1]=="":
        button_2.config(text="X")
        button_2.update_idletasks()
        vsepozicije[1]="X"
        igralec_X = False
    elif igralec_X == False and vsepozicije[1]=="":
        button_2.config(text="O")
        button_2.update_idletasks()
        vsepozicije[1]="O"
        igralec_X = True
    checkwin()


def button_3():
    global vsepozicije
    global igralec_X
    if igralec_X == True and vsepozicije[2]=="":
        button_3.config(text="X")
        button_3.update_idletasks()
        vsepozicije[2]="X"
        igralec_X = False
    elif igralec_X == False and vsepozicije[2]=="":
        button_3.config(text="O")
        button_3.update_idletasks()
        vsepozicije[2]="O"
        igralec_X = True
    checkwin()
    


def button_4():
    global vsepozicije
    global igralec_X
    if igralec_X == True and vsepozicije[3]=="":
        button_4.config(text="X")
        button_4.update_idletasks()
        vsepozicije[3]="X"
        igralec_X = False
    elif igralec_X == False and vsepozicije[3]=="":
        button_4.config(text="O")
        button_4.update_idletasks()
        vsepozicije[3]="O"
        igralec_X = True
    checkwin()


def button_5():
    global vsepozicije
    global igralec_X
    if igralec_X == True and vsepozicije[4]=="":
        button_5.config(text="X")
        button_5.update_idletasks()
        vsepozicije[4]="X"
        igralec_X = False
    elif igralec_X == False and vsepozicije[4]=="":
        button_5.config(text="O")
        button_5.update_idletasks()
        vsepozicije[4]="O"
        igralec_X = True
    checkwin()


def button_6():
    global vsepozicije
    global igralec_X
    if igralec_X == True and vsepozicije[5]=="":
        button_6.config(text="X")
        button_6.update_idletasks()
        vsepozicije[5]="X"
        igralec_X = False
    elif igralec_X == False and vsepozicije[5]=="":
        button_6.config(text="O")
        button_6.update_idletasks()
        vsepozicije[5]="O"
        igralec_X = True
    checkwin()

def button_7():
    global vsepozicije
    global igralec_X
    if igralec_X == True and vsepozicije[6]=="":
        button_7.config(text="X")
        button_7.update_idletasks()
        vsepozicije[6]="X"
        igralec_X = False
    elif igralec_X == False and vsepozicije[6]=="":
        button_7.config(text="O")
        button_7.update_idletasks()
        vsepozicije[6]="O"
        igralec_X = True
    checkwin()

def button_8():
    global vsepozicije
    global igralec_X
    if igralec_X == True and vsepozicije[7]=="":
        button_8.config(text="X")
        button_8.update_idletasks()
        vsepozicije[7]="X"
        igralec_X = False
    elif igralec_X == False and vsepozicije[7]=="":
        button_8.config(text="O")
        button_8.update_idletasks()
        vsepozicije[7]="O"
        igralec_X = True
    checkwin()

def button_9():
    global vsepozicije
    global igralec_X
    if igralec_X == True and vsepozicije[8]=="":
        button_9.config(text="X")
        button_9.update_idletasks()
        vsepozicije[8]="X"
        igralec_X = False
    elif igralec_X == False and vsepozicije[8]=="":
        button_9.config(text="O")
        button_9.update_idletasks()
        vsepozicije[8]="O"
        igralec_X = True
    checkwin()



button_1 = ttk.Button(root, text="", style="Custom.TButton",command=button_1, width=20)
button_1.grid(column=0, row=0, sticky=E)

button_2 = ttk.Button(root, text="", style="Custom.TButton", width=20,command=button_2)
button_2.grid(column=1, row=0, sticky=E)

button_3 = ttk.Button(root, text="", style="Custom.TButton", width=20,command=button_3)
button_3.grid(column=2, row=0, sticky=E)

button_4 = ttk.Button(root, text="", style="Custom.TButton", width=20,command=button_4)
button_4.grid(column=0, row=1, sticky=E)

button_5 = ttk.Button(root, text="", style="Custom.TButton", width=20,command=button_5)
button_5.grid(column=1, row=1, sticky=E)

button_6 = ttk.Button(root, text="", style="Custom.TButton", width=20,command=button_6)
button_6.grid(column=2, row=1, sticky=E)

button_7 = ttk.Button(root, text="", style="Custom.TButton", width=20,command=button_7)
button_7.grid(column=0, row=2, sticky=E)

button_8 = ttk.Button(root, text="", style="Custom.TButton", width=20,command=button_8)
button_8.grid(column=1, row=2, sticky=E)

button_9 = ttk.Button(root, text="", style="Custom.TButton", width=20,command=button_9)
button_9.grid(column=2, row=2, sticky=E)



root.mainloop()
