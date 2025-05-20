import tkinter as tk

root = tk.Tk()
root.geometry('700x700')



label_question = tk.Label(root, text='Dobrodosli v kvizu', font=('Arial', 20))
label_question.pack(fill=tk.BOTH)

answer_framer = tk.Frame(root)
answer_framer.pack(padx=10, pady=10) 

def  on_click_button_1():
    global points
    button_answer_1.config(state='disable')
    button_answer_2.config(state='disable')
    button_answer_3.config(state='disable')
        
    if answers [current_question] [0] == 1:
        points += 1
        label_status.config( text='Pravilno si odgovoril !')
    else:
         label_status.config( text='Narobe si odgovoril !')

    button_continue.config( text='Nadaljuj', state='active')
   
def  on_click_button_2():
    global points
    button_answer_1.config(state='disable')
    button_answer_2.config(state='disable')
    button_answer_3.config(state='disable')
    if answers [current_question] [0] == 2:
        points += 1
        label_status.config( text='Pravilno si odgovoril !')
    else:
         label_status.config( text='Narobe si odgovoril !')

    button_continue.config( text='Nadaljuj', state='active')
   

def  on_click_button_3():
    global points
    button_answer_1.config(state='disable')
    button_answer_2.config(state='disable')
    button_answer_3.config(state='disable')
    if answers [current_question] [0] == 3:
        points += 1
        label_status.config( text='Pravilno si odgovoril !')
        button_continue.config( text='Nadaljuj', state='active')
    else:
         label_status.config( text='Narobe si odgovoril !')
         
    button_continue.config( text='Nadaljuj', state='active')
   




button_answer_1 = tk.Button (answer_framer, text='prvi odgovor', state='disabled', command=on_click_button_1, font=('Arial', 20))
button_answer_2 = tk.Button (answer_framer, text='drugi odgovor', state='disabled', command=on_click_button_2, font=('Arial', 20))
button_answer_3 = tk.Button (answer_framer, text='tretji odgovor', state='disabled', command=on_click_button_3, font=('Arial', 20))

button_answer_1.pack(side=tk.LEFT, padx=10)
button_answer_2.pack(side=tk.LEFT, padx=10)
button_answer_3.pack(side=tk.LEFT, padx=10)

label_status = tk.Label (root, text='  ', font=('Arial', 20))
label_status.pack()

def on_click_continue():
    global current_question, ending
    if ending == True:
        root.destroy()
        return
    if current_question == -1:
        button_continue.config( text='nadaljuj', state='disabled')
   
    label_status.config(text=' ')

     
    current_question += 1
   

    if current_question < len (question):
        button_answer_1.config(state='active')
        button_answer_2.config(state='active')
        button_answer_3.config(state='active')
    else:
        label_status.config(text=f'Dosegli ste {points} od {len(question) } tock')
        button_continue.config( text='koncaj', state='active')
        ending = True
        return

    
    button_answer_1.config(text=answers[current_question] [1] )
    button_answer_2.config(text=answers[current_question] [2] )
    button_answer_3.config(text=answers[current_question] [3] )

    label_question.config(text=question [current_question])



ending = False 
current_question = -1
points = 0

button_continue = tk.Button(root, text='zacni', command=on_click_continue, font=('Arial', 20))
button_continue.pack()

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

question = [
    'Katera je najvecja gora v sloveniji?',
    'Kako je ime avtorju zdravljice?',
    'Katerega leta se je slovenija osamosvojila?',
    'Kako se imenuje največji ocean na svetu?',
    'Koliko celin je na Zemlji?',
    'Kateri element ima kemijsko oznako O?',
    'Kaj proučuje ornitologija?',
    'Kdo je bil prvi predsednik samostojne Slovenije?',
    'Kdaj se je začela prva svetovna vojna?',
    'Kdaj se je začela druga svetovna vojna?',
    'Kdo je bil slavni francoski vojskovodja, ki je postal cesar?',
    'Kje je bil podpisan mirovni sporazum po prvi svetovni vojni?',
    'Kdo je bil rimski diktator, ki je bil umorjen leta 44 pr. n. št.?',
    'Katera civilizacija je izumila klinopis?',
    'Kdo je bil prvi predsednik Združenih držav Amerike?',
    'Kateri zid je ločeval Vzhodni in Zahodni Berlin?',
    'Katera kraljica je znana po dolgi vladavini v 19. stoletju v Veliki Britaniji?',
    'Kateri narod je zgradil Machu Picchu?',
    'Kdo je izrekel znani stavek: “Imam sanje”?',
    

]

answers = [
    [2, 'Stol', 'Triglav', 'Mont Blanc'],
    [2, 'Josip Jurcic' , 'Frnce Preseren', 'Ivan Cankar'],
    [1, '1991', '1990', '1992'],
    [3, 'Atlantski ocean', 'Indiski ocean', 'Tihi ocean'],
    [1, '7', '5', '3'],
    [1, 'kisik', 'vodik', 'helji'],
    [2, 'rastlinami', 'ptiči', 'sesalci'],
    [3, 'Janez Janša', 'Borut Pahor', 'Milan Kučan'],
    [1, '1914', '1924', '1918'],
    [1, '1939', '1929', '1945'],
    [2, 'Ludvik XIV', 'Napoleon Bonaparte', 'Karel Veliki'],
    [1, 'Versailles', 'Berlin', 'Dunaj'],
    [2, 'August Oktavijan', 'Julij Cezar', 'Mark Antonij'],
    [2, 'Egipčani', 'Sumerci', 'Grki'],
    [2, ' Abraham Lincoln', 'George Washington', 'Thomas Jefferson'],
    [1, 'Berlinski zid', 'Kitajski zid', 'Rimski zid'],
    [2, 'Elizabeta I', 'Viktorija', ' Marija Tudor'],
    [3, 'Nelson Mandela', 'Barack Obama', 'Martin Luther King Jr.']



    
]















root.mainloop()






