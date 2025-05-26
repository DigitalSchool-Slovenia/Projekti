


#idle množenje
#dolzina = "20"
#dolzina_stranice = 20

#dolzina_input_int =input("stevilka1:")
#dolzina_input_int = int(dolzina_input)
#dolzina_input_int =int(dolzina_input_int)
#print(dolzina_stranice, dolzina)


#dolzina_input_int2 =input("stevilka2:")
#dolzina_input_int2 = int(dolzina_input)
#dolzina_input_int2 =int(dolzina_input_int2)
#print(dolzina_stranice, dolzina)

#print("Ploščina:", dolzina_input_int * dolzina_input_int )

#ploščina = dolzina_input_int *dolzina_input_int
#print( "Ploščina:", ploščina)
#print(f"Ploščina je: {ploščina}")




#neki druzga'''''???????

#print("Rezulat:" , št * št2 )
#št = dolzina_input_int * dolzina_input_int
#št2 = dolzina_input_int2 + dolzina_input_int2
#print( "št:" , št)
#print( "št2:" , št2)
#print(f"Rezultat je: {št * št2 * št+št2} ")



#stvar



   #naloga
#dolzina_input_int3 = input("stevilka3")
#dolzina_input_int3 =int(dolzina_input_int3)


#dolzina_input_int4 = input("stevilka4")
#dolzina_input_int4 =int(dolzina_input_int4)

#if (dolzina_input_int3 > dolzina_input_int4):
    #print(" ni uredu")
 
#else (dolzina_input_int3 < dolzina_input_int4):
    #print (" vstop ")


#naloga2
#dolzina_input_int5 = input("stevilka5")
#dolzina_input_int5 =int(dolzina_input_int5)
#print(dolzina_input_int5 %7)


#if (dolzina_input_int5 ==1):
    #print(" ponedeljek")
     
#if (dolzina_input_int5 ==2):
    #print("torek")

#if (dolzina_input_int5 ==3):
    #print(" sreda")

#if (dolzina_input_int5 ==4):
   # print("Četrtek")

#if (dolzina_input_int5 ==5):
    #print(" petek")

#if (dolzina_input_int5 ==6):
   #
#if (dolzina_input_int5 ==7):
    #print(" nedelja")



# koledar?


#mat naloga

#starost1 = int(input("vnesi st"))
#starost2 = int(input("vnest st2"))
#znak = input("vnest znak")

#if (znak == "+"):
    #print( starost1 + starost2)

#if (znak == "-"):
    #print( starost1 - starost2)

#if (znak == "*"):
 #   print( starost1 * starost2)

#if (znak == "/"):
    #print(starost1 / 


#seznam = [1,2,3,4,5]
#vsota = 0


#for element in seznam :
    #vsota = vsota + element
#print(vsota)

#dolzina = len(seznam)
#povprecna = vsota / dolzina









#import random

#poteza_moja =input("napis st od 0 do 2")
#poteza_st = (random.randint(0,3))



#print(random.randint(100,1000))
 
#if random.randint(100,1000)== 777:
    #print("jackpot")

#else:
   # print("skill ishue")




















"""

import random

seznam_izidov = [0,0,0]

for i in range(3):
    seznam_potez = ["skarje","kamen","papir"]

    poteza_racunalnika = random.choice(seznam_potez)
    poteza_igralca = input("napisi svoj odgovor :")
    print("racunalnik je napisal :",poteza_racunalnika)

    if poteza_igralca == poteza_racunalnika:
        print("neodloceno")
        seznam_izidov[1]+= 1
    if poteza_igralca == "skarje" and poteza_racunalnika == "kamen":
        print("zgubis")
        seznam_izidov[0]+= 1
    if poteza_igralca == "kamen" and poteza_racunalnika == "skarje":
        print("zmagas")
        seznam_izidov[2]+= 1

    if poteza_igralca == "skarje" and poteza_racunalnika == "papir":
        print("zmaga")
        seznam_izidov[2]+= 1

    if poteza_igralca == "papir" and poteza_racunalnika == "skarje":
        print("zgubis")
        seznam_izidov[0]+= 1
    
    if poteza_igralca == "kamen" and poteza_racunalnika == "papir":
        print("zgubis")
        seznam_izidov[0]+= 1

    if poteza_igralca == "papir" and poteza_racunalnika == "kamen":
        print("zmagas")
        seznam_izidov[2]+= 1


print("racunalnik :", seznam_izidov[0])
print("izenačeno :", seznam_izidov[1])
print("jaz :", seznam_izidov[2])
"""

"""
seznam_stevil

for i in range(10):
    seznam_stevil.append(random.randint(0,100))

for i in range(10):
    stevilo = seznam_stevil[i]
    naslednje = seznam_stevil[i + 1]
    print(stevilo)
    guess = input("Ugibaj naslednje stevilo:" )

if(guess < naslednje):
    print("st je manjse")


else:
    print("st je vecje")


    """







"""

st_imen = int(input("Vnesi stevilo :"))


seznam_imen = []
seznam_prisotnosti=(seznam_imen)




for i in range(st_imen):
    
    prebrano_ime = input("VPIŠI IME :")
    
    seznam_imen.append(prebrano_ime)
    
    print(seznam_imen)


#nal 2

for i in range(st_imen):
    print(i + 1 ,"." , seznam_imen[i])




for i in range(st_imen):

    prebrana_prisotnost = input("Vnesi " + seznam_imen[i] + " prisotnost:")

    seznam_prisotnosti.append(prebrana_prisotnost)

"""
















"""

#nal 3

skupina1 = []

skupina2 = []

skupina3 = []

for i in range(len(seznam_imen)):
    
 if i%3 == 0:
    skupina1.append(seznam_imen[i])
    

 if i%3 == 1:
   skupina2.append(seznam_imen[i])
    

 if i%3 == 2:
   skupina3.append(seznam_imen[i])


print("skupina 1:", skupina1)
print("skupina 2:", skupina2)
print("skupina 3:", skupina3)

#4nal


"""
"""
import turtle


import colorsys


t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
n = 70
h = 0
for i in range (360):
    c = colorsys.hsv_to_rgb(h, 1,0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range (2):
        t.left(2)
        t.circle(170)

"""
"""


from turtle import *
import colorsys
bgcolor('black')
tracer (500)

def draw():
    h = 0
    for i in range(100):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 0.5
        up()
        goto(0,0)
        down()
        color('black')
        fillcolor (c)
        begin_fill()
        rt (98)
        circle(i, 12)
        fd (290)
        fd (i)
        lt (29)
        for j in range (129):
            fd(i)
            circle(j, 299, steps=2)
        end_fill()

draw()
done()


"""



import random
import pygame
import math

pygame.init()
pygame.font.init()
 
font = pygame.font.SysFont("Times New Roman", 40)
 
WIDTH = 1080
HEIGHT = 620
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shooter")
 
# Spremenljivke, ki jih bomo potrebovali za igralca
# ---
class Ammo_pack:
    def __init__(self, x, y):
        self.position = pygame.Rect(x,y,75,50)
        
        self.image = pygame.image.load("ammo.png")
        self.image = pygame.transform.scale(self.image, (75, 50))

        self.picked_up = False

    def pick_up(self):
        player.bullets += 6
        self.picked_up = True
        
    def draw (self, player):
        x_relative = self.position.x - (player.position.x - player.x_relative)
        y_relative = self.position.y - (player.position.y - player.y_relative)

        window.blit(self.image, pygame.Rect(x_relative, y_relative, self.position.width, self.position.height))
        


    

class Bullet:
    next_id = 0
    def __init__(self, x, y, direction):
        self.position = pygame.Rect(x, y, 10, 10)
        self.direction = direction
        self.id = Bullet.next_id
        Bullet.next_id += 1
        self.damage = 10
        self.remove = False

    def __eq__(self,other):
        return self.id == other.id
        
    def move(self):
        self.position.x += self.direction[0]
        self.position.y += self.direction[1]
        for platform in platforms:
            if self.position.colliderect(platform.position):
                self.remove = True
                break
        for demon in demons:
            if self.position.colliderect(demon.position):
                self.remove = True
                demon.health -= 5
                break

        if math.sqrt((self.position.x - player.position.x)**2 +(self.position.y - player.position.y)**2)>1000:
            self.remove = True
            return

    def draw (self, player):
        x_relative = self.position.x - (player.position.x - player.x_relative)
        y_relative = self.position.y - (player.position.y - player.y_relative)
        
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(x_relative, y_relative, self.position.width, self.position.height))

        
            

class Demon:
    move_speed = 2
    attack_delay = 0
    def __init__(self,x,y):
        self.size = 75
        self.position = pygame.Rect(x, y, self.size, self.size)
        self.image = pygame.image.load("images2.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.damage = 5
        self.health = 20
        self.speed_x = 0
        self.speed_y = 0

    def move(self, player):
        direction = player.position.x-self.position.x
        if direction > 0:
            self.speed_x = Demon.move_speed
        elif direction < 0:
            self.speed_x = -Demon.move_speed
        else:
            self.speed_x = 0

        if self.speed_y < 20:
            self.speed_y += 1

        self.position.x += self.speed_x
        self.position.y += self.speed_y

        if abs(player.position.x - self.position.x) < abs( player.position.y - self.position.y)and( player.position.y < self.position.y - 20):
            self.speed_y = -18

        

        for platform in platforms:
            if self.position.colliderect(platform.position):
                self.resolve_collision(platform.position)

        if self.position.colliderect(player.position)and Demon.attack_delay <= 0:
            player.health -= self.damage
            Demon.attack_delay = 120
        Demon.attack_delay -= 1
    
    #ko umre ti da 3 metka
    
   
    #lahko dropajo health


    def draw(self):
        x_relative = self.position.x - (player.position.x - player.x_relative)
        y_relative = self.position.y - (player.position.y - player.y_relative)
        
        window.blit(self.image, pygame.Rect(x_relative, y_relative, self.position.width, self.position.height))


    def resolve_collision(self, rect_b):
        rect_a = self.position

        dx1 = rect_b.right - rect_a.left
        dx2 = rect_a.right - rect_b.left
        dy1 = rect_b.bottom - rect_a.top
        dy2 = rect_a.bottom - rect_b.top
     
        
        min_dx = min(dx1, dx2)
        min_dy = min(dy1, dy2)
     
        if min_dx < min_dy:
            
            if dx1 < dx2:
                rect_a.x += dx1  # Move right
            else:
                rect_a.x -= dx2  # Move left
        else:
            
            if dy1 < dy2:
                pass
                # player.speed_y = 0
                # rect_a.y += dy1  # Move down
            else:
                rect_a.y -= dy2  # Move up
        
        return True  # Collision was resolved
        
   

        
class Player:
    def __init__(self, x, y):
        self.size = 75
        self.position = pygame.Rect(x, y, self.size, self.size)
        self.image = pygame.image.load("doom.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.speed_x = 0
        self.speed_y = 0
        self.jumps = 2
        self.bullets = 10
        self.direction = 0
        self.x_relative = (WIDTH - self.size) // 2
        self.y_relative = 3 * (HEIGHT - self.size) // 4
        self.health = 100
        self.score = 0
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.speed_x = 5
            self.direction = 1
        elif keys[pygame.K_a]:
            self.speed_x = -5
            self.direction = -1
        else:
            self.speed_x = 0
 
        if keys[pygame.K_SPACE] and self.jumps > 0 and self.speed_y > -5:
            self.jumps -= 1
            self.speed_y = -18
 
        if self.speed_y < 20:
            self.speed_y += 1
 
        self.position.x += self.speed_x
        self.position.y += self.speed_y

        if self.position.y >=2000:
            player.health = 0
 
        # if self.position.x < 0:
        #     self.position.x = 0
        # if self.position.x > WIDTH - self.size:
        #     self.position.x = WIDTH - self.size
        # if self.position.y < 0:
        #     self.position.y = 0
        # if self.position.y > HEIGHT - self.size:
        #     self.position.y = HEIGHT - self.size
        
        for platform in platforms:
            if self.position.colliderect(platform.position):
                resolve_collision(self.position, platform.position)
 
    def draw(self):
        if (player.direction > 0):
            window.blit(pygame.transform.flip(player.image, True, False), (self.x_relative, self.y_relative))
        else:
            window.blit(self.image, (self.x_relative, self.y_relative))

        pygame.draw.rect(window,(133, 131, 127), (0, HEIGHT-50,250, 50 ))
        font_render= font.render(f"{self.health}% health",False, (127,0,0))
        window.blit(font_render,(5,HEIGHT-45))

        pygame.draw.rect(window,(133, 131, 127), (220, HEIGHT-50,180, 50 ))
        font_render= font.render(f"{self.bullets} ammo",False, (127,0,0))
        window.blit(font_render,(225,HEIGHT-45))

        pygame.draw.rect(window,(133, 131, 127), (400, HEIGHT-50,150, 50 ))
        font_render= font.render(f"{self.score} score",False, (127,0,0))
        window.blit(font_render,(400,HEIGHT-45))
 
class Platform:
    def __init__(self, x, y, width, height):
        self.position = pygame.Rect(x, y, width, height)
 
    def draw(self, player):
        x_relative = self.position.x - (player.position.x - player.x_relative)
        y_relative = self.position.y - (player.position.y - player.y_relative)
        
        pygame.draw.rect(window, (54, 74, 49), pygame.Rect(x_relative, y_relative, self.position.width, self.position.height))



demon_count = 2

player = Player(600, 300)
demons =[]
ammo_packs =[]
 
platforms = [Platform(-2000, 1200, 4000, 50)]
for x in range(-2000, 2000, 300):
    platform = Platform(x, random.randint(900, 1100),200, 20)
    platforms.append(platform)

bullets = []


# ---
 
def resolve_collision(rect_a, rect_b):
    # Compute overlap distances in x and y
    dx1 = rect_b.right - rect_a.left
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
            pass
            # player.speed_y = 0
            # rect_a.y += dy1  # Move down
        else:
            player.jumps = 2
            player.speed_y = 0
            rect_a.y -= dy2  # Move up
    
    return True  # Collision was resolved

def spawn_demon(player):
    px = player.position.x + random.randint(300, 400)*(random.choice([-1,1]))
    py = player.position.y - random.randint(0, 400)
    demon = Demon(px,py)
    demons.append(demon)

spawn_delay = 600
# Glavna zanka igre
clock = pygame.time.Clock()
counter = 0
running = True
while running:
    counter += 1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
    
            direction = [
                position[0] - player.x_relative,
                position[1] - player.y_relative,
            ]

            length = math.sqrt(direction[0]**2 + direction[1]**2) /10
            direction[0]/= length
            direction[1]/= length
            if player.bullets > 0:
                
                player.bullets -= 1
                
                bullets.append(Bullet(player.position.x, player.position.y, direction))
        if event.type == pygame.QUIT:
            running = False
 
    window.fill((166, 165, 161))
    # background_image = pygame.image.load("images/New Piskel.png")
    # background_image = pygame.transform.scale(background_image, (width, height))
    # window.blit(background_image, (0, 0))
    # Premikanje igralčevega lika
    # ---
 
    # Vsako ponovitev zanke (vsak frame) dobimo pritisnjene tipke
    # in se glede na njih odločimo, kako bomo igralca premaknili
 
    player.move()

    for demon in demons:
        demon.move(player)
   
   
    if spawn_delay < 0:
        spawn_delay = 5000
        Demon.move_speed += 0.1
        demon_count += 0.5
       
        
        for i in range(random.randint(1,int(demon_count))):
            spawn_demon(player)
    
 
  
    for bullet in bullets:
        bullet.move()
        
        

    bullets = [b for b in bullets if not b.remove]

    for ammo_pack in ammo_packs:
        if ammo_pack.position.colliderect(player.position):
            ammo_pack.pick_up()

        
   
    for d in demons:
        if d.health <= 0:
            ammo_pack = Ammo_pack(d.position.x,d.position.y +25)
            ammo_packs.append(ammo_pack)
            player.score += 1
    
    demons = [d for d in demons if d.health > 0]

    ammo_packs = [a for a in ammo_packs if not a.picked_up]

    
    for bullet in bullets:
        bullet.draw(player)
    
    for platform in platforms:
        platform.draw(player)

    for demon in demons:
        demon.draw()

    for ammo_pack in ammo_packs:
        ammo_pack.draw(player)

    if player.health<= 0:
        running = False

    player.draw()
        # window.blit(slika_ovire, platform)
 
    # ---
 
    pygame.display.update()
    dt = clock.tick(60)
    spawn_delay -= dt

image_game_over = pygame.image.load("death2.png")
window.blit(image_game_over, pygame.Rect(0,0,WIDTH, HEIGHT))
pygame.display.update()
  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()



