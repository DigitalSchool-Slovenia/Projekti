import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 800  # Increased world size
TILE_SIZE = 40
ROWS, COLS = HEIGHT // TILE_SIZE, WIDTH // TILE_SIZE
HOTBAR_HEIGHT = 50
BLOCK_TYPES = [1, 2, 3, 4, 5, 6, 7]

# Colors for blocks
textures = {
    1: (139, 69, 19),   # Dirt (Brown)
    2: (34, 139, 34),   # Grass (Green)
    3: (128, 128, 128), # Stone (Gray)
    4: (139, 90, 43),   # Wood (Dark Brown)
    5: (237, 201, 175), # Sand (Beige)
    6: (0, 0, 255),     # Water (Blue)
    7: (0, 255, 0),     # Nuclear Reactor (Glowing Green)
    8: (50, 50, 50)     # Bedrock (Dark Gray)
}

# Initialize window
window = pygame.display.set_mode((WIDTH, HEIGHT + HOTBAR_HEIGHT))
pygame.display.set_caption("2D Minecraft Clone")

current_block = 1  # Default block to place (dirt)

# Generate terrain
def generate_terrain():
    terrain = []
    for y in range(ROWS):
        row = []
        for x in range(COLS):
            if y == ROWS - 1:
                row.append(8)  # Bedrock at the bottom
            elif y == ROWS // 2:
                row.append(2)  # Grass layer
            elif y > ROWS // 2:
                row.append(1 if random.random() > 0.2 else 3)  # Dirt or stone
            else:
                row.append(0)  # Air
        terrain.append(row)
    return terrain

grid = generate_terrain()

# Player class
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE * 2)
        self.speed_x = 0
        self.speed_y = 0
        self.onground = False
        self.in_water = False
        self.health = 100
        self.last_y = y

    def move(self, keys):
        self.speed_x = 0
        if keys[pygame.K_a]:
            self.speed_x = -5
        if keys[pygame.K_d]:
            self.speed_x = 5
        if keys[pygame.K_SPACE]:
            if self.onground:
                self.speed_y = -12
            elif self.in_water:
                self.speed_y = -4

    def apply_gravity(self):
        if self.in_water:
            self.speed_y += 0.5
            if self.speed_y > 3:
                self.speed_y = 3
        else:
            if not self.onground:
                self.speed_y += 1
            if self.speed_y > 10:
                self.speed_y = 10

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.onground = False
        self.in_water = False

        fall_distance = self.last_y - self.rect.y
        if self.onground and fall_distance > TILE_SIZE * 3:
            self.health -= max(0, (fall_distance // TILE_SIZE - 2) * 5)
            if self.health <= 0:
                print("Steve has died!")
                pygame.quit()
                exit()
        self.last_y = self.rect.y

        for y in range(ROWS):
            for x in range(COLS):
                tile_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if grid[y][x] != 0:
                    if self.rect.colliderect(tile_rect):
                        if grid[y][x] == 6:
                            self.in_water = True
                        elif grid[y][x] == 7:
                            print("BOOM! You exploded!")
                            pygame.quit()
                            exit()
                        elif self.speed_y > 0:
                            self.rect.bottom = tile_rect.top
                            self.speed_y = 0
                            self.onground = True

player = Player(WIDTH // 2, HEIGHT // 2)

def draw_hotbar():
    pygame.draw.rect(window, (50, 50, 50), (0, HEIGHT, WIDTH, HOTBAR_HEIGHT))
    for i, block in enumerate(BLOCK_TYPES):
        color = textures[block]
        pygame.draw.rect(window, color, (i * 60 + 10, HEIGHT + 10, 50, 30))
        if block == current_block:
            pygame.draw.rect(window, (255, 255, 255), (i * 60 + 10, HEIGHT + 10, 50, 30), 2)

def draw_health_bar():
    pygame.draw.rect(window, (200, 0, 0), (10, 10, player.health * 2, 20))
    pygame.draw.rect(window, (255, 255, 255), (10, 10, 200, 20), 2)

# Game loop
running = True
while running:
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.apply_gravity()
    player.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_7:
                current_block = event.key - pygame.K_0
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            grid_y, grid_x = y // TILE_SIZE, x // TILE_SIZE
            if event.button == 3 and y < HEIGHT:
                grid[grid_y][grid_x] = current_block
            elif event.button == 1 and y < HEIGHT:
                grid[grid_y][grid_x] = 0
    
    window.fill((0, 162, 232))
    
    for y in range(ROWS):
        for x in range(COLS):
            block_type = grid[y][x]
            if block_type != 0:
                pygame.draw.rect(window, textures[block_type], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    pygame.draw.rect(window, (255, 215, 0), (player.rect.x, player.rect.y, TILE_SIZE, TILE_SIZE * 2))  # Steve character
    draw_hotbar()
    draw_health_bar()
    
    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()
