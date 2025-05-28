import pygame
import random
pygame.init()
pygame.font.init()

width = 1800
height = 1000

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Are you scared already? 'Cause Duo'll finish you!")

 
# Spremenljivke, ki jih bomo potrebovali za igralca
# ---

class Coin:
    def __init__ (self, x, y, image):
        self.position = pygame.Rect(x, y, 50, 50)
        self.image = pygame.transform.scale(pygame.image.load(image), (50, 50))


class Player:
    def __init__(self, x, y, height, width, image, left, right, jump):
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.position = pygame.Rect(x, y, self.width, self.height)
        self.speed_x = 0
        self.speed_y = 0
        self.on_ground = False
        self.keybinds = {
            "left" : left,
            "right" : right,
            "jump" : jump
            }
        self.score = 0
        self.knife = False
        
    def move(self, keys):
        if keys[self.keybinds["right"]]:
            self.speed_x = 3
        elif keys[self.keybinds["left"]]:
            self.speed_x = -3
        else:
            self.speed_x = 0
            
        if keys[self.keybinds["jump"]] and self.on_ground == True: 
            self.on_ground = False
            self.speed_y = -15

        if self.speed_y < 30:
            self.speed_y += 0.75

        self.position.x += self.speed_x
        self.position.y += self.speed_y
     
        if self.position.x < 0:
            self.position.x = 0
        if self.position.x > width - self.width:
            self.position.x = width - self.width
        if self.position.y < 0:
            self.position.y = 0
        if self.position.y > height - self.height:
            self.position.y = height - self.height
    
    def resolve_collision(self, rect_b):
        # Compute overlap distances in x and y
        rect_a = self.position
        dx1 =  - (rect_a.left - rect_b.right)
        dx2 = rect_a.right - rect_b.left
        dy1 = rect_b.bottom - rect_a.top
        dy2 = rect_a.bottom - rect_b.top
     
        # Find the smallest displacement to separate them
        min_dx = min(dx1, dx2)
        min_dy = min(dy1, dy2)
     
        if min_dx < min_dy:
            # Move rect_a left or right
            if dx1 < dx2:
                rect_a.x += dx1  # Move right
            else:
                rect_a.x -= dx2  # Move left
        else:
            # Move rect_a up or down
            if dy1 < dy2:
                rect_a.y += dy1  # Move down
            else:
                self.on_ground = True
                self.speed_y = 0
                rect_a.y -= dy2  # Move up
        
        return True  # Collision was resolved

    def getpoint(self):
        text = f"Score: {self.score}"
        self.img = font.render(text, True, BLACK)


duo = Player(10, 50, 50, 50, "images/duolingo.png", pygame.K_a, pygame.K_d, pygame.K_w)
you = Player(1700, 750, 50, 80, "images/you.png", pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)
coins = [Coin(225, 100,  "images/golden_knife.png")]






# pygame.Rect(random.randint(0, 1725), random.randint(0, 1050), 75, 10)

portals = [pygame.Rect(1790, 700, 10, 75)]    

obsticles = [pygame.Rect(0, 990, 1800, 100), #tla
             pygame.Rect(0, 75, 100, 20), pygame.Rect(1690, 775, 110, 20), #kjer se spawnata
             ]

for i in range(9):
    obsticles.append(pygame.Rect(random.randint(155, 1655), 180, 75, 10))
for i in range(7):
    obsticles.append(pygame.Rect(random.randint(80, 1655), 270, 75, 10))
for i in range(6):
    obsticles.append(pygame.Rect(random.randint(80, 1655), 360, 75, 10))
for i in range(7):
    obsticles.append(pygame.Rect(random.randint(80, 1655), 450, 75, 10))
for i in range(7):
    obsticles.append(pygame.Rect(random.randint(80, 1655), 540, 75, 10))
for i in range(6):
    obsticles.append(pygame.Rect(random.randint(80, 1655), 630, 75, 10))
for i in range(6):
    obsticles.append(pygame.Rect(random.randint(80, 1580), 720, 75, 10))
for i in range(7):
    obsticles.append(pygame.Rect(random.randint(80, 1655), 810, 75, 10))
for i in range(6):
    obsticles.append(pygame.Rect(random.randint(80, 1655), 900, 75, 10))

# ---



 

# Glavna zanka igre
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    window.fill((164, 237, 183))
    
    
    keys = pygame.key.get_pressed()
    duo.move(keys)
    you.move(keys)
        
   
    for obsticle in obsticles:
        if duo.position.colliderect(obsticle):
            duo.resolve_collision(obsticle)

    for obsticle in obsticles:
        if you.position.colliderect(obsticle):
            you.resolve_collision(obsticle)

    if duo.position.colliderect(you.position) and duo.knife:
        duo.score += 1
        duo.position.x = 10
        duo.position.y = 10
        you.position.x = 1700
        you.position.y = 710

    for coin in coins:
        if duo.position.colliderect(coin.position):
            coins.remove(coin)
            duo.image = pygame.transform.scale(pygame.image.load("images/duo_lipa.png"), (50, 50))
            duo.knife = True
            
    for portal in portals:
        if you.position.colliderect(portal):
            you.position.x = 10
            you.position.y = 50
        

    font = pygame.font.SysFont("Arial.ttf", 50)
    duo.img = font.render(f'Score: {duo.score}', True, (67, 181, 29))
    window.blit(duo.img, (10, 950))


    # ---
    # Izris likov
    # ---

    window.blit(duo.image, duo.position)
    window.blit(you.image, you.position)

    for obsticle in obsticles:
        pygame.draw.rect(window, (67, 181, 29), obsticle)

    for portal in portals:
        pygame.draw.rect(window, (1, 100, 35), portal)

    for coin in coins:
        window.blit(coin.image, coin.position)

# !!!!! score !!!! pa mnj gravitacije ---- naslednjic
 
 
    # ---
 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
