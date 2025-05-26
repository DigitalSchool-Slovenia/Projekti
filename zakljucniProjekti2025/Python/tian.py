import pygame
pygame.init()
wieth = 1000
high = 600
pygame.font.init()
font = pygame.font.SysFont("Times New Roman",50)
import time  
window = pygame.display.set_mode((wieth, high))
pygame.display.set_caption("Platformer Game")
 
# Spremenljivke, ki jih bomo potrebovali za igralca

# ---
game_running = True
rekord = 0

while game_running:
    player_high = 75
    player_wieth = 75
    player2_high =100
    player2_wieth = 100

    player_image = pygame.image.load("realmadrid.webp")
    player_image = pygame.transform.scale(player_image, (player_wieth, player_high))
    player = pygame.Rect(100, 300, player_wieth, player_high )
    player_image2 = pygame.image.load("letalo.JPG")
    player_image2 = pygame.transform.scale(player_image2, (player2_wieth, player2_high))
    player2 = pygame.Rect(1000, 0, player2_wieth, player2_high)
    player_image0 = pygame.image.load("konec2.PNG")
    player_image0 = pygame.transform.scale(player_image0, (1000, 600))
    player0 = pygame.Rect(1500, 300, 1000, 600)
    speed = 0
    import random
    seznam = ["a","b","c","č","d","e","f","g","h","i","j","k", "l"]
    random.shuffle(seznam)
    a = seznam.pop()

    # ---
    Rezultat = 0



    # Glavna zanka igre
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                running = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                speed = -10
            
     
        window.fill((135, 206, 235))
        
        # Premikanje igralčevega lika
        # ---
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            speed = -10
        if keys[pygame.K_UP]:
            game_running = False
            running = False
            break
        speed += 0.75
        player.y += speed
        c = 20
        player2.x -= c
        if Rezultat % 10 == 0 :
            c += 3
        
        
        
        
        
        # ---

        if player2.x < 100:
            Rezultat += 1
            seznam.append(a)
            random.shuffle(seznam)
            a = seznam.pop()
            
            if a == "a":
                player2.x = 1000
                player2.y = 0
            if a == "b":
                player2.x = 1000
                player2.y = 100
            if a == "c":
                player2.x = 1000
                player2.y = 200
            if a == "č":
                player2.x = 1000
                player2.y = 300
            if a == "d":
                player2.x = 1000
                player2.y = 400
            if a == "e":
                player2.x = 1000
                player2.y = 500
            if a == "f":
                player2.x = 1000
                player2.y = 500
            if a == "g":
                player2.x = 1000
                player2.y = 500
            if a == "h":
                player2.x = 1000
                player2.y = 0
            if a == "i":
                player2.x = 1000
                player2.y = 0
            if a == "j":
                player2.x = 1000
                player2.y = 500
            if a == "k":
                player2.x = 1000
                player2.y = 0
                
        if player.colliderect(player2):
            player0 = pygame.Rect(0 , 0, 1000 , 600)
            running = False
            print("Rezultat je:" , Rezultat)    
        # Izris likov
        # ---
        if player.y < 0:
            player.y = 0
        if player.y > 600 - 70:
            player.y = 530
            speed = 0
        # ---
        
        window.blit(player_image, player)
        window.blit(player_image2, player2)
        window.blit(player_image0, player0)
        font_render = font.render(f"Rezultat je : {Rezultat}" , False , (0 , 200 , 0))
        font_render3 = font.render("Za novo igro pocakajte 3 sekunde" , False , (255 , 255 , 255))
        font_render2 = font.render("Za ustavitev igre pritisnite tipko UP" , False , (255 , 255 , 255))
        if running == False :
            window.blit(font_render3, (200, 400 ))
            window.blit(font_render2, (200, 500 ))
        font_render1 = font.render(f"Rekord : {rekord}" , False , (0 , 200 , 0))
        window.blit(font_render, (0, 0 ))
        
        window.blit(font_render1, (0, 50 ))

        if Rezultat > rekord :
            rekord = Rezultat
        
        pygame.display.update()
        clock.tick(60)
    
    time.sleep(3)
    



pygame.quit()
