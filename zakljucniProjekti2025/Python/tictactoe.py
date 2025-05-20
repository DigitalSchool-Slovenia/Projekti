import tkinter as tk
 
tile = 0
square = 0
turn = 0
smllsquare = 0
 
root = tk.Tk()
root.geometry('900x900')


 
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

gameover_text = tk.Label(root, text="", font=("Arial", 20), bg="white", fg="red")

canvas.create_rectangle(1, 1, 900, 900, width=10, outline='black')
 
 
 
canvas.create_line(300, 1, 300, 900, width=5)
canvas.create_line(600, 1, 600, 900, width=5)
 
canvas.create_line(1, 300, 900, 300, width=5)
canvas.create_line(1, 600, 900, 600, width=5)
 
 
canvas.create_line(100, 1, 100, 900, width=2)
canvas.create_line(200, 1, 200, 900, width=2)
canvas.create_line(400, 1, 400, 900, width=2)
canvas.create_line(500, 1, 500, 900, width=2)
canvas.create_line(700, 1, 700, 900, width=2)
canvas.create_line(800, 1, 800, 900, width=2)
 
canvas.create_line(1, 100, 900, 100, width=2)
canvas.create_line(1, 200, 900, 200, width=2)
canvas.create_line(1, 400, 900, 400, width=2)
canvas.create_line(1, 500, 900, 500, width=2)
canvas.create_line(1, 700, 900, 700, width=2)
canvas.create_line(1, 800, 900, 800, width=2)
 
#0-> igra traja; 1-> igralec 1 zmaga; 2-> igralec 2 zmaga
gamestates = [
    [0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0]
]
 
playing_square = -1
 
 
tiles_state = [
    [ [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ] ], 
    [ [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ] ],
    [ [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ] ]
]    

PROGRAM_STATE = 'PLAYING'
 
 
def  is_smllsquare_zero(square, tile):
    return tiles_state[square[0]][square[1]][tile[0]][tile[1]] == 0
 
def  is_square_active(square):
    return gamestates[square[0]][square[1]] == 0
 
def check_square_gameover(square_state):
    for i in range(3):
        if all(square_state[i][j] == 1 for j in range(3)):
            return (i, 0), (i, 2), 1
        if all(square_state[i][j] == 2 for j in range(3)):
            return (i, 0), (i, 2), 2
 
    for j in range(3):
        if all(square_state[i][j] == 1 for i in range(3)):
            return (0, j), (2, j), 1
        if all(square_state[i][j] == 2 for i in range(3)):
            return (0, j), (2, j), 2
 
    if all(square_state[i][i] == 1 for i in range(3)):
        return (0, 0), (2, 2), 1
    if all(square_state[i][i] == 2 for i in range(3)):
        return (0, 0), (2, 2), 2
 
    if all(square_state[i][2-i] == 1 for i in range(3)):
        return (2, 0), (0, 2), 1
    if all(square_state[i][2-i] == 2 for i in range(3)):
        return (2, 0), (0, 2), 2
 
    return None
 
def check_gameover():
    for i in range(3):
        for j in range(3):
            if gamestates[i][j] != 0:
                continue
            state = check_square_gameover(tiles_state[i][j])
 
            if state is not None:
                start, stop, player = state
                gamestates[i][j] = player
                return i, j, start, stop
    return None
 
 
def on_click(event):
    global turn
    global tile
    global square
    global smllsquare
    global playing_square
    global PROGRAM_STATE

    if PROGRAM_STATE != 'PLAYING':
        print('game ended')
        return
 
    x = event.x
    y = event.y
 
    a = (y//300) + 1
    b = (x//300) + 1
    square = [a - 1, b - 1]
 
    e = (y//100) + 1
    f = (x//100) + 1
 
    if a == 2:
        c = 3
    elif a == 3:
        c = 6
    else:
        c = 0
 
 
    if b == 2:
        d = 3
    elif b == 3:
        d = 6
    else:
        d = 0
 
 
    tile = [e - c -1, f - d - 1]
    smllsquare = [e - 1, f - 1]

    if not is_square_active(square):
        print('Game not active in this square anymore.')
        return
    elif playing_square != -1 and 3 * square[0] + square[1] != playing_square:
        print('Invalid playing square')
        return
    elif not is_smllsquare_zero(square, tile):
        print('Tile was already played before')
        return
    
 
 
    print('square-->', square)
    print('tile-->', tile)
    print('smllsquare-->', smllsquare)
    print(turn)
    print('')

    # set the tile as clicked by the active player
    tiles_state[square[0]][square[1]][tile[0]][tile[1]] = turn + 1
    print(tiles_state)

    # draw the additional tile
    draw(smllsquare)

    # set playing square based on the last selected tile
    playing_square = 3 * tile[0] + tile[1]
    if not is_square_active(tile):
        playing_square = -1

    # check every square if the gameover condition is met
    state = check_gameover()
    print(gamestates)
    if state is not None:
        playing_square = -1
        
        gameover_squarey, gameover_squarex = state[0], state[1]
        start_tiley, start_tilex = state[2]
        stop_tiley, stop_tilex = state[3]
        canvas.create_line((gameover_squarex*300 + start_tilex*100 + 50),
                           (gameover_squarey*300 + start_tiley*100 + 50),
                           (gameover_squarex*300 + stop_tilex*100 + 50),
                           (gameover_squarey*300 + stop_tiley*100 + 50),
                           fill='black', width=10)

    # check the gameover squares if the final gameover condition is met
    state = check_square_gameover(gamestates)
    if state is not None:
        if state[2] == 1:
            PROGRAM_STATE = 'PLAYER 1 WON'
        else:
            PROGRAM_STATE = 'PLAYER 2 WON'
        
        gameover_text.place(relx=0.5, rely=0.5, anchor="center")
        gameover_text.config(text=PROGRAM_STATE)
        
        start, end, player = state
        start_squarey, start_squarex = start
        end_squarey, end_squarex = end
        canvas.create_line((start_squarex*300 + 150),
                           (start_squarey*300 + 150),
                           (end_squarex*300 + 150),
                           (end_squarey*300 + 150),
                           fill='orange', width=20)
        
 
    turn = turn + 1
 
    if turn > 1:
        turn = 0
 
 
 
 
def križec(x, y):
    canvas.create_line((x - 35), (y - 35), (x + 35), (y + 35), fill='red', width=5)
    canvas.create_line((x - 35), (y + 35), (x + 35), (y - 35), fill='red', width=5)
 
def krožec(x, y):
    canvas.create_oval((x - 35), (y - 35), (x + 35), (y + 35), outline='aqua', width=5)
 
def draw(smllsquare):
    global turn
    a = 100
    x = ((smllsquare[1] + 1) * a) - 50
    y = ((smllsquare[0] + 1)* a) - 50
 
    print(x, y)
 
 
    if turn == 1:
        križec(x, y)
 
 
    if turn == 0:
        krožec(x, y)
 
 
 
 
 
 
 
 
 
 
root.bind("<Button-1>", on_click,)
 
root.mainloop()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#križec--> red
#krožec--> aqua
 
 
