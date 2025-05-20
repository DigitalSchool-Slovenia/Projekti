import tkinter as tk
import random 
import time

seq = [0,1,2,3]
selected_seq = []
root = tk.Tk()
root.title("Whac-A-Mole")
root.geometry ("300x300")
canvas = tk.Canvas(root, bg="#e1e2ff")
canvas.pack(fill=tk.BOTH, expand=True)
global tocke, kjejekrt
kjejekrt = [0, 0, 0, 0]
tocke = 0

def kvadrat (xpos, ypos, stranica):
    canvas.create_rectangle( xpos, ypos, xpos + stranica, ypos + stranica, width=5, outline="#409c7b")

def krog (x1, y1, x2, y2):
    canvas.create_oval(x1, y1, x2, y2, width=5, fill="#f01dde", outline="#7300ff")


def naredi_krta ():
    global kjejekrt 
    krt = [[120, 120, 180, 180 ],[20, 20, 80, 80], [220, 220, 280, 280],
        [220, 120, 280, 180], [120, 220, 180, 280], [20, 220, 80, 280],
        [20, 120, 80, 180], [120, 20, 180, 80], [220, 20, 280, 80]]

    x = random.randint(0, 8)
        

    krog (krt[x][0],krt[x][1], krt[x][2], krt[x][3])
    kjejekrt = krt[x]


def narisan_okvir ():
    canvas.delete('all')
    kvadrat (0, 0, 100)
    kvadrat (100, 100, 100)
    kvadrat (0, 200, 100)
    kvadrat (100, 200, 100)
    kvadrat (200, 200, 100)
    kvadrat (200, 100, 100)
    kvadrat (200, 0, 100)    
    naredi_krta()
    root.after(5000, narisan_okvir)

narisan_okvir()





def on_click (event):
    global kjejekrt, tocke 
    if event.x >= kjejekrt[0] and event.y >= kjejekrt[1] and event.x <= kjejekrt[2] and event.y <= kjejekrt[3]:
        narisan_okvir()
        tocke +=1
        print("Zadeli ste! Točke so:")
        print (tocke)

root.bind('<Button-1>', on_click)


root.mainloop()

