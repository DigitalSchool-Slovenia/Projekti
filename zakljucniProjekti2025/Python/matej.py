import random
import pygame
import math
import time

pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Times New Roman", 30)
big_font = pygame.font.SysFont("Times New Roman", 200)

WIDTH, HEIGHT = 1300, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

class GrapplingHook:
    def __init__(self):
        self.position = None
        self.attached = False
        self.speed = 10  # You can lower this value for smoother movement if desired

    def shoot(self, target_pos):
        self.position = list(target_pos)
        self.attached = True

    def update(self, player):
        if self.attached and self.position:
            dx = self.position[0] - player.position.x
            dy = self.position[1] - player.position.y
            distance = math.sqrt(dx**2 + dy**2)

            if distance > 5:
                # Move the player gradually toward the hook position
                player.position.x += dx / distance * self.speed
                player.position.y += dy / distance * self.speed
            else:
                self.attached = False

    def draw(self, player):
        if self.attached and self.position:
            pygame.draw.circle(window, (255, 0, 0), self.position, 5)
            pygame.draw.line(window, (255, 0, 0), (player.x_relative, player.y_relative), self.position, 2)

class Coin:
    def __init__(self, x, y, image_path):
        self.position = pygame.Rect(x, y, 50, 42)
        self.image = pygame.transform.scale(pygame.image.load(image_path), (50, 50))
        self.score = 1 if "bakren" in image_path else 2 if "srebrn" in image_path else 3

    def collect(self, player):
        player.score += self.score

    def draw(self, player):
        x_relative = self.position.x - (player.position.x - player.x_relative)
        y_relative = self.position.y - (player.position.y - player.y_relative)
        window.blit(self.image, (x_relative, y_relative))

class Platform:
    def __init__(self, x, y, width, height, colour):
        self.position = pygame.Rect(x, y, width, height)
        self.colour = colour

    def draw(self, player):
        x_relative = self.position.x - (player.position.x - player.x_relative)
        y_relative = self.position.y - (player.position.y - player.y_relative)
        pygame.draw.rect(window, self.colour, 
                         pygame.Rect(x_relative, y_relative, self.position.width, self.position.height))

class Player:
    def __init__(self, x, y):
        self.size = 101
        self.position = pygame.Rect(x, y, self.size, self.size)
        self.image = pygame.image.load("mario.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.speed_x, self.speed_y = 0, 0
        self.jumps, self.score, self.direction = 6, 0, 0
        self.x_relative = (WIDTH - self.size) // 2
        self.y_relative = 3 * (HEIGHT - self.size) // 4

    def move(self, grappling_hook):
        keys = pygame.key.get_pressed()
        if not grappling_hook.attached:  # Normal movement only when not using the hook
            if keys[pygame.K_d]:
                self.speed_x = 15
                self.direction = 1
            elif keys[pygame.K_a]:
                self.speed_x = -15
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

    def draw(self):
        window.blit(self.image, (self.x_relative, self.y_relative))

# Updated collision resolution: now accepts player and the colliding platform's rect
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
            rect_a.y += dy1  # Move down
            player.speed_y = 0
        else:
            player.jumps = 3
            player.speed_y = 0
            rect_a.y -= dy2  # Move up



        

def generate_level():
    platforms = [
        Platform(5000, 0, 600, 20000, (0, 0, 0)),  # Right border
        Platform(-5000, 0, 600, 20000, (0, 0, 0)),  # Left border
        Platform(-5000, -3000, 20000, 600, (0, 0, 0)),  # Bottom border
        Platform(-5000, 3000, 20000, 600, (0, 0, 0))   # Top border
    ]
    y = 1000 - 50
    for _ in range(750):
        x = random.randint(-5000, 5000)
        y -= random.randint(-1000, 1000)
        platforms.append(Platform(x, y, random.randint(300, 700), random.randint(20, 30), (0, 0, 0)))
    return platforms

# New non-blocking timer function using pygame.time.get_ticks()
def get_time_remaining(start_time, duration):
    elapsed = (pygame.time.get_ticks() - start_time) // 1000
    return max(0, duration - elapsed)

player = Player(100, 100)
grappling_hook = GrapplingHook()

# Coins generation (preserving your original coin creation)
coins = (
    [Coin(random.randint(-5000, 5000), random.randint(-700, 800), "bakren_kovanec.png") for _ in range(100)]
    + [Coin(random.randint(-5000, 5000), random.randint(-700, 800), "srebrn_kovanec.png") for _ in range(50)]
    + [Coin(random.randint(-5000, 5000), random.randint(-700, 800), "zlat_kovanec.png") for _ in range(25)]
)

platforms = generate_level()

# Timer settings
timer_duration =60  # seconds
start_time = pygame.time.get_ticks()

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
            # grappling_hook.shoot(event.pos)

    window.fill((255, 255, 0))
    player.move(grappling_hook)
    grappling_hook.update(player)

    # Draw platforms and resolve collisions with the player
    for platform in platforms:
        if player.position.colliderect(platform.position):
            resolve_collision(player.position, platform.position)
        platform.draw(player)

    # Process coins: collect if collided and then draw
    for coin in coins[:]:  # iterating over a shallow copy for safe removal
        if player.position.colliderect(coin.position):
            coin.collect(player)
            coins.remove(coin)
        coin.draw(player)

    player.draw()
    grappling_hook.draw(player)

    # Display score
    score_text = font.render(f"Score: {player.score}", False, (0, 0, 0))
    window.blit(score_text, (10, 10))

    # Display remaining time using a non-blocking timer
    time_remaining = get_time_remaining(start_time, timer_duration)
    timer_text = font.render(f"Time Remaining: {time_remaining}", False, (0, 0, 0))
    window.blit(timer_text, (600, 10))

    # End the game if time runs out
    if time_remaining == 0:
        if player.score >= 100:
            window.fill ((255, 255, 255))
            win_text = big_font.render(f"YOU WON WITH A SCORE OF: {player.score}!", False, (0, 0, 0)) 
            window.blit(win_text, (0, 0))
            pygame.display.update()
            time.sleep(5)
            running = False
        else:
            window.fill ((255, 255, 255))
            lose_text = big_font.render(f"YOU LOST: {100 - player.score}!", False, (0, 0, 0 ))
            window.blit(lose_text, (0, 0))
            pygame.display.update()
            time.sleep(5) 
            running = False
 
    pygame.display.update()
    clock.tick(60)

pygame.quit()
