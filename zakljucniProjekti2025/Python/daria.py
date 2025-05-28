BlockingIOError
import pygame
import random

pygame.init()



windowWidth = 1650
windowHeight = 900
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Summer Fruit Temple")
platforms = [pygame.Rect(100, 200, 1400, 70),
             pygame.Rect(0, 400, 1400, 70),
             pygame.Rect(200, 600, 1650, 70),
             pygame.Rect(0, 800, 1650, 70)]
             

vrata = pygame.Rect(1250, 83, 100, 120)
vrataImage = pygame.image.load("vrata.png")
vrataImage = pygame.transform.scale(vrataImage, (100, 120))
tla = pygame.Rect(0, 200, 1650, 700)
tlaImage = pygame.image.load("plaza.png")
tlaImage = pygame.transform.scale(tlaImage, (1650, 700))


backgroundImage = pygame.image.load("sky.png")
backgroundImage = pygame.transform.scale(backgroundImage, (windowWidth, windowHeight))

    
class Player:
    def __init__(self, x, y, image, up, left, right, width, height):
        self.position = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.speedX = 0
        self.speedY = 0
        self.onGround = False
        self.direction = 0
        self.up = up
        self.left = left
        self.right = right


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.right]:
            self.speedX = 20
            self.direction = 1
        elif keys[self.left]:
            self.speedX = -20
            self.direction = -1
        else:
            self.speedX = 0
 
        if keys[self.up] and self.onGround == True:
            self.onGround = False
            self.speedY = -22
 
        if self.speedY < 30:
            self.speedY += 1

        self.position.x += self.speedX
        self.position.y += self.speedY

        if self.position.x < 0:
            self.position.x = 0
        if self.position.x > windowWidth - self.position.width:
            self.position.x = windowWidth - self.position.width
        if self.position.y < 0:
            self.position.y = 0
        if self.position.y > windowHeight - self.position.height:
            self.position.y = windowHeight - self.position.height
        
        for platform in platforms:
            if self.position.colliderect(platform):
                self.resolve_collision(self.position, platform)

    def resolve_collision(self,rect_a, rect_b):
        # Compute overlap distances in x and y
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
                self.speedY = 0
                rect_a.y += dy1  # Move down
            else:
                rect_a.y -= dy2
                self.onGround = True # Move up
    
    #return True  # Collision was resolved

limona = Player(2000, 700, "limona.png",pygame.K_w, pygame.K_a, pygame.K_d, 100, 120)
lubenica = Player(2000, 700, "lubenica.png", pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, 100, 70)

# ---


# Glavna zanka igre
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(backgroundImage, (0, 0))
# Premikanje igralčevega lika
    lubenica.move()
    limona.move()
 
    # ---
 
    # Izris likov
    
            
    window.blit(vrataImage, vrata)
    if (limona.direction < 0):
        window.blit(pygame.transform.flip(limona.image, True, False), limona.position)
    else:
        window.blit(limona.image, limona.position)

    if (lubenica.direction < 0):
        window.blit(pygame.transform.flip(lubenica.image, True, False), lubenica.position)
    else:
        window.blit(lubenica.image, lubenica.position)

    for platform in platforms:
        pygame.draw.rect(window, (150, 150, 10), platform)

    window.blit(tlaImage, tla)

    if limona.position.colliderect(vrata) and lubenica.position.colliderect(vrata):
        backgroundImage = pygame.image.load("youwinscreen.png")
        backgroundImage = pygame.transform.scale(backgroundImage, (windowWidth, windowHeight))
        window.blit(backgroundImage, (0, 0))
 # ---
    
 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
#________________________________________________________________________________________________________________________________________________________
