import pygame
import random
import math
pygame.init()


#def rot_center(image, angle):
    #rot_image = pygame.transform.rotate(image, angle)

HEIGHT, WIDTH = 1000,1000
BOX_size = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman but fake")

angle_deg = 0
angle_rad = math.radians(angle_deg)

green = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

apple_image = pygame.image.load("Food_for_fake_pac_man-removebg-preview.png")
apple_compres = pygame.transform.scale(apple_image, (BOX_size, BOX_size))
head_img = pygame.image.load("pecman.png")
head_compres = pygame.transform.scale(head_img, (BOX_size, BOX_size))
Krog_trail = pygame.image.load("yalow.png") 
trail_compres = pygame.transform.scale(Krog_trail, (BOX_size, BOX_size))
rotated_image = head_compres

Pacman = [(200, 200), (100, 200), (0, 200)]
direction = (BOX_size, 0)
Pacman_hitbox = BOX_size
Trail_hitbox = BOX_size
Apple_hitbox = BOX_size

formula = (950//BOX_size) 

def apple():
    x = random.randint(0, formula)*BOX_size
    y = random.randint(0, formula)*BOX_size
    print(x,y)
    return (x, y)

apple1 = apple()


clock = pygame.time.Clock()


running = True
while running:
    clock.tick(8)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != (0, BOX_size):
                direction = (0, -BOX_size)
                rotated_image = pygame.transform.rotate(head_compres, 90)
            if event.key == pygame.K_a and direction != (BOX_size, 0):
                direction = (-BOX_size, 0)
                rotated_image = pygame.transform.rotate(head_compres, 180)
            if event.key == pygame.K_d and direction != (-BOX_size, 0):
                direction = (BOX_size, 0)
                rotated_image = pygame.transform.rotate(head_compres, 0)
            if event.key == pygame.K_s and direction != (0, -BOX_size):
                direction = (0, BOX_size)
                rotated_image = pygame.transform.rotate(head_compres, 270)
        
    new_head = (Pacman [0] [0] + direction [0], Pacman [0] [1] + direction [1])        
    Pacman.insert (0, new_head)        


    x, y = new_head               


    if x < 0:
      running = False
    if y < 0:
      running = False
    if x > WIDTH:
      running = False
    if y > HEIGHT:
      running = False


    if new_head in Pacman[1:]:
       running = False

    if new_head == apple1:
      apple1 = apple()
    else :
      Pacman.pop() 


    screen.fill(black)
    screen.blit(apple_compres, apple1)
    screen.blit(rotated_image, Pacman[0])

    for segment in Pacman[1:]:
      screen.blit(trail_compres, segment)



    pygame.display.update()

pygame.quit() 