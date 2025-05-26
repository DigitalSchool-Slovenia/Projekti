import pygame 

pygame.init() 

window = pygame.display.set_mode((1000, 1000)) 

class Sprite:  




    def __init__(self,width,height,x,y,image): 

        self.y = y 

        self.x = x 

        self.image = pygame.image.load(image) 

        self.image = pygame.transform.scale(self.image, (width, height)) 

running = True 

 
pygame.font.init()
font = pygame.font.SysFont(None, 100)  # You can adjust size here

lines = Sprite(5,1000,338,5,"images.png") 

lines1 = Sprite(5,1000,674,5,"images.png") 

lines2 = Sprite(1000,5,5,338,"images.png") 

lines3 = Sprite(1000,5,5,674,"images.png") 

clock = pygame.time.Clock() 

xoro = True 

running = True 

b1utton_rect = pygame.Rect(0,0,338,338) 

x1 = Sprite(323,323,0,0,"39-512.webp") 

o1 = Sprite(323,323,0,0,"images (1).png") 

b2utton_rect = pygame.Rect(338,0,338,338) 

x2 = Sprite(323,323,338,0,"39-512.webp") 

o2 = Sprite(323,323,338,0,"images (1).png") 

b3utton_rect = pygame.Rect(674,0,338,338) 

x3 = Sprite(323,323,674,0,"39-512.webp") 

o3 = Sprite(323,323,674,0,"images (1).png") 

b4utton_rect = pygame.Rect(0,338,338,338) 

x4 = Sprite(323,323,0,338,"39-512.webp") 

o4 = Sprite(323,323,0,338,"images (1).png") 

b5utton_rect = pygame.Rect(338,338,338,338) 

x5 = Sprite(323,323,338,338,"39-512.webp") 

o5 = Sprite(323,323,338,338,"images (1).png") 

b6utton_rect = pygame.Rect(674,338,338,338) 

x6 = Sprite(323,323,674,338,"39-512.webp") 

o6 = Sprite(323,323,674,338,"images (1).png") 

b7utton_rect = pygame.Rect(0,674,338,338) 

x7 = Sprite(323,323,0,674,"39-512.webp") 

o7 = Sprite(323,323,0,674,"images (1).png") 

b8utton_rect = pygame.Rect(338,674,338,338) 

x8 = Sprite(323,323,338,674,"39-512.webp") 

o8 = Sprite(323,323,338,674,"images (1).png") 

b9utton_rect = pygame.Rect(674,674,338,338) 

x9 = Sprite(323,323,674,674,"39-512.webp") 

o9 = Sprite(323,323,674,674,"images (1).png")


b1_filled = False
b1_content = None

b2_filled = False
b2_content = None

b3_filled = False
b3_content = None

b4_filled = False
b4_content = None

b5_filled = False
b5_content = None

b6_filled = False
b6_content = None

b7_filled = False
b7_content = None

b8_filled = False
b8_content = None

b9_filled = False
b9_content = None

def check_winner():
    win_combos = [
        [b1_content, b2_content, b3_content],  # Top row
        [b4_content, b5_content, b6_content],  # Middle row
        [b7_content, b8_content, b9_content],  # Bottom row
        [b1_content, b4_content, b7_content],  # Left column
        [b2_content, b5_content, b8_content],  # Middle column
        [b3_content, b6_content, b9_content],  # Right column
        [b1_content, b5_content, b9_content],  # Diagonal from top-left
        [b3_content, b5_content, b7_content]   # Diagonal from top-right
    ]

    for combo in win_combos:
        if combo[0] is not None and combo[0] == combo[1] == combo[2]:
            return combo[0]  
    return None



 

while running: 

    for event in pygame.event.get(): 

        if event.type == pygame.QUIT: 

            running = False 

    window.fill((255, 255, 255)) 

    if event.type == pygame.MOUSEBUTTONDOWN:
        if b1utton_rect.collidepoint(event.pos) and not b1_filled:
            if xoro:
                b1_content = "O"
                xoro = False
            else:
                b1_content = "X"
                xoro = True
            b1_filled = True

        if b2utton_rect.collidepoint(event.pos) and not b2_filled:
            if xoro:
                b2_content = "O"
                xoro = False
            else:
                b2_content = "X"
                xoro = True
            b2_filled = True

        if b3utton_rect.collidepoint(event.pos) and not b3_filled:
            if xoro:
                b3_content = "O"
                xoro = False
            else:
                b3_content = "X"
                xoro = True
            b3_filled = True

        if b4utton_rect.collidepoint(event.pos) and not b4_filled:
            if xoro:
                b4_content = "O"
                xoro = False
            else:
                b4_content = "X"
                xoro = True
            b4_filled = True

        if b5utton_rect.collidepoint(event.pos) and not b5_filled:
            if xoro:
                b5_content = "O"
                xoro = False
            else:
                b5_content = "X"
                xoro = True
            b5_filled = True

        if b6utton_rect.collidepoint(event.pos) and not b6_filled:
            if xoro:
                b6_content = "O"
                xoro = False
            else:
                b6_content = "X"
                xoro = True
            b6_filled = True

        if b7utton_rect.collidepoint(event.pos) and not b7_filled:
            if xoro:
                b7_content = "O"
                xoro = False
            else:
                b7_content = "X"
                xoro = True
            b7_filled = True

        if b8utton_rect.collidepoint(event.pos) and not b8_filled:
            if xoro:
                b8_content = "O"
                xoro = False
            else:
                b8_content = "X"
                xoro = True
            b8_filled = True

        if b9utton_rect.collidepoint(event.pos) and not b9_filled:
            if xoro:
                b9_content = "O"
                xoro = False
            else:
                b9_content = "X"
                xoro = True
            b9_filled = True
    if b1_filled:
        if b1_content == "X":
            window.blit(x1.image, (x1.x, x1.y))
        else:
            window.blit(o1.image, (o1.x, o1.y))

    if b2_filled:
        if b2_content == "X":
            window.blit(x2.image, (x2.x, x2.y))
        else:
            window.blit(o2.image, (o2.x, o2.y))

    if b3_filled:
        if b3_content == "X":
            window.blit(x3.image, (x3.x, x3.y))
        else:
            window.blit(o3.image, (o3.x, o3.y))

    if b4_filled:
        if b4_content == "X":
            window.blit(x4.image, (x4.x, x4.y))
        else:
            window.blit(o4.image, (o4.x, o4.y))

    if b5_filled:
        if b5_content == "X":
            window.blit(x5.image, (x5.x, x5.y))
        else:
            window.blit(o5.image, (o5.x, o5.y))

    if b6_filled:
        if b6_content == "X":
            window.blit(x6.image, (x6.x, x6.y))
        else:
            window.blit(o6.image, (o6.x, o6.y))

    if b7_filled:
        if b7_content == "X":
            window.blit(x7.image, (x7.x, x7.y))
        else:
            window.blit(o7.image, (o7.x, o7.y))

    if b8_filled:
        if b8_content == "X":
            window.blit(x8.image, (x8.x, x8.y))
        else:
            window.blit(o8.image, (o8.x, o8.y))

    if b9_filled:
        if b9_content == "X":
            window.blit(x9.image, (x9.x, x9.y))
        else:
            window.blit(o9.image, (o9.x, o9.y))
    window.blit(lines.image, (lines.x,lines.y)) 

    window.blit(lines1.image, (lines1.x,lines1.y)) 

    window.blit(lines2.image, (lines2.x,lines2.y)) 

    window.blit(lines3.image, (lines3.x,lines3.y)) 



    
    winner = check_winner()
    if winner:
        text = font.render(f"{winner} wins!", True, (0, 0, 0))
        window.blit(text, (500, 450))  
        pygame.display.update()
        pygame.time.delay(3000)  
        running = False

    pygame.display.update() 

    clock.tick(60) 

 
