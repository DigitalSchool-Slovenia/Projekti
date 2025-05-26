import pygame
import random
pygame.init()
 
width = 1200
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Platformer Game")
 


 
class Player:
    def __init__(self, x, y):
        self.size = 75
        self.position = pygame.Rect(x, y, self.size, self.size)
        self.image = pygame.image.load("geometrydash.png")#
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.speed_x = 0
        self.speed_y = 0
        
class Enemy:
    def __init__(self):
        self.height = 100
        self.widht = 200
        self.position = pygame.Rect(random.randint(0,width-self.widht), -self.height, self.widht, self.height)
        self.image = pygame.image.load("dado.jpg")#
        self.image = pygame.transform.scale(self.image, (self.widht,self.height))

    def move(self):
        self.position.y+=10
        
    
 
player = Player(100, 100)

enemies = []


 
def resolve_collision(rect_a, rect_b):
  
    dx1 = rect_b.right - rect_a.left
    dx2 = rect_a.right - rect_b.left
    dy1 = rect_b.bottom - rect_a.top
    dy2 = rect_a.bottom - rect_b.top
 
  
    min_dx = min(dx1, dx2)
    min_dy = min(dy1, dy2)
 
    if min_dx < min_dy:
       
        if dx1 < dx2:
            rect_a.x += dx1  
        else:
            rect_a.x -= dx2
    else:
     
        if dy1 < dy2:
            rect_a.y += dy1  
        else:
            rect_a.y -= dy2  
    return True  
 
timer = 0
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    window.fill((110, 130, 70))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.speed_x = 5
    elif keys[pygame.K_LEFT]:
        player.speed_x = -5
    else:
        player.speed_x = 0

    player.position.y = height - player.position.height
 
 
 
    player.position.x += player.speed_x

    if player.position.x < 0:
        player.position.x = 0
    if player.position.x > width - player.size:
        player.position.x = width - player.size
    if player.position.y < 0:
        player.position.y = 0
    if player.position.y > height - player.size:
        player.position.y = height - player.size

    timer-=1
    if timer < 0:
        enemies.append(Enemy())
        timer = 30
    
    for enemy in enemies:
        enemy.move()
        if player.position.colliderect(enemy.position):
            running = False
    
   

 
    window.blit(player.image, player.position)
    for enemy in enemies:
        window.blit(enemy.image, enemy.position)
        
     
 

 
    pygame.display.update()
    clock.tick(60)

game_over = pygame.image.load("game.over.jpg")
game_over = pygame.transform.scale(game_over,(width,height))
window.blit(game_over,(0,0))
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
 
pygame.quit()
