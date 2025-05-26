import pygame
import random
import time
import sys

#icializacija Pygame
pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Times New Roman", 20)
font_navodila = pygame.font.SysFont("Times New Roman", 15)
font_gameover = pygame.font.SysFont("Times New Roman", 40)



# Nastavitve okna
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Avto Igra: Izogibaj se avtomobilom!")

# Barve
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Nastavitve igralca
player_width = 60
player_height = 60
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 95

# Nastavitve nasprotnikov
enemy_width = 60
enemy_height = 50
#enemy_speed = 5
enemy_frequency = 30  # Pogostost generiranja nasprotnikov (nižja številka = pogosteje)

# Naloži slike
player_image = pygame.image.load("player2.png")  # Pot do tvoje slike avtomobila
player_image = pygame.transform.scale(player_image, (player_width, player_height))

enemy_image = pygame.image.load("nasprotnik.png")  # Pot do slike nasprotnega avtomobila
enemy_image = pygame.transform.scale(enemy_image, (enemy_width, enemy_height))

road_image = pygame.image.load("pixelroad.png")  # Pot do slike ceste
road_image = pygame.transform.scale(road_image, (screen_width, screen_height))

eksplozija_image = pygame.image.load("eksplozija.png")  # Pot do slike ceste
eksplozija_image = pygame.transform.scale(eksplozija_image, (60, 60))

# Ura za obvladovanje števila sličic na sekundo
clock = pygame.time.Clock()

# Funkcija za risanje igralca
def draw_player(x, y):
    screen.blit(player_image, (x, y))

# Funkcija za risanje nasprotnikov
def draw_enemy(x, y):
    screen.blit(enemy_image, (x, y))

# Funkcija za generiranje nasprotnikov
def generate_enemy():
    x_pos = random.choice([30, 120, 200, 300])  # Dva pasova, na katerih se bodo pojavljali nasprotniki
    y_pos = -enemy_height
    return [x_pos, y_pos]

# Funkcija za premikanje nasprotnikov
def move_enemy(enemy_list, speed):
    for enemy in enemy_list:
        enemy[1] += speed
    enemy_list = [enemy for enemy in enemy_list if enemy[1] < screen_height]  # Odstrani nasprotnike, ki so izven zaslona
        
    return enemy_list

#score = 0
# Glavna zanka igre
def game_loop():
    game_over = False
    player_x = 125
    player_y = screen_height - player_height - 100
    player_x_change = 0
    hitrost_igre = 60

    enemies = []
    enemy_timer = 0

    score=0

    navodila = "Premikaj se z puščicami. Izogibaj se avtom in peljanju s ceste!"
    konec_igre = "KONEC IGRE! (klikni Q za izhod, in R za ponovni poskus)"
    velikost_navodil = 80
    navodila_rect = pygame.Rect(0,screen_height - velikost_navodil, screen_width, velikost_navodil)

    enemy_speed = 5

    y_position = 0
    scroll_speed = 4

    #last_score_checkpoint = 0
    
    #while not game_over:
    while 1:
        # Dogodk
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Premikanje igralca
            #keys = pygame.key.get_pressed()
            if hitrost_igre != 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:  # Pazi na pasove (200 je prvi pas)
                        player_x -= player_speed
                    elif event.key == pygame.K_RIGHT:  # Pazi na pasove
                        player_x += player_speed
                    
        y_position += scroll_speed
        if y_position >= screen_height:
            y_position = 0

        if hitrost_igre != 0:
            screen.blit(road_image, (0, y_position))
            screen.blit(road_image, (0, y_position - screen_height))  # Ponavljanje ozadja
        
        
        #player_x += player_x_change
        #if player_x<0 or player_x + player_width > screen_width:
            #hitrost_igre = 0
        if hitrost_igre != 0:
            if player_x<0:
                player_x += 60
                hitrost_igre = 0
                screen.blit(eksplozija_image, (player_x, player_y - 10))
                draw_player(player_x, player_y)

            elif player_x>screen_width:
                player_x -= 60
                hitrost_igre = 0
                screen.blit(eksplozija_image, (player_x, player_y - 10))
                draw_player(player_x, player_y)

            #game_over = True
        # Generiranje nasprotnikov
        enemy_timer += 0.5
        if enemy_timer >= enemy_frequency:
            enemies.append(generate_enemy())
            enemy_timer = 0

        #if score%10==0:
            #enemy_speed += 5
        # Premikanje nasprotnikov
        enemies = move_enemy(enemies, enemy_speed)

        # Risanje na zaslon
        #screen.fill(BLACK)
        #screen.blit(road_image, (0, 0))  # Nariši cesto v ozadju
        if hitrost_igre != 0:
            draw_player(player_x, player_y)

        for enemy in enemies:
            draw_enemy(enemy[0], enemy[1])
            #if enemy[1] ?? screnheight score+=1:
            if enemy[1] == screen_height - 5:
                score += 1


                
            

        # Preverjanje trkov
        for enemy in enemies:
            if player_x < enemy[0] + enemy_width and player_x + player_width > enemy[0]:
                if player_y < enemy[1] + enemy_height and player_y + player_height > enemy[1]:
                    game_over = True  # Trk z nasprotnikom, konec igre
                    hitrost_igre = 0
                    screen.blit(eksplozija_image, (player_x, player_y - 10))

            

        #Izris Rezultata        
        score_text= font.render(f"ČAS: {score}", True, (100,200,50))

        

        #Izris Navodil in game over
        pygame.draw.rect(screen,(0,0,0), navodila_rect)
        navodila_text = font_navodila.render(navodila, True, (255, 255, 255))
        text_rect = navodila_text.get_rect(center=navodila_rect.center)
        screen.blit(navodila_text, text_rect)
        screen.blit(score_text, (10, 570))

        if hitrost_igre == 0:
            enemy_speed = 0
            pygame.draw.rect(screen,(0,0,0), navodila_rect)
            navodila_text = font_navodila.render(konec_igre, True, (255, 255, 255))
            text_rect = navodila_text.get_rect(center=navodila_rect.center)
            screen.blit(navodila_text, text_rect)
            screen.blit(score_text, (170, 570))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        pygame.quit()
                        sys.exit(0)
                    elif event.key == pygame.K_r:
                        game_loop()
 
                        

        
        # Osvežitev zaslona
        pygame.display.update()
        #pygame.display.flip()

        # Nastavitev FPS
        clock.tick(hitrost_igre)

    # Ko je igra končana
    #pygame.quit()

# Zaženi igro
game_loop()
