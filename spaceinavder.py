import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHAR_X_POS = 350
CHAR_Y_POS = 500
ENEMYSTART_Y_MIN = 50
ENEMYSTART_Y_MAX = 150
ENEMYX_SPEED = 5
ENEMYY_SPEED = 50
BULLET_SPEED = 10
COLLISION_DISTANCE = 30

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")
icon =pygame.image.load("bg.png")
pygame.display.set_icon(icon)
playerimg = pygame.image.load("player.png")
player_x = CHAR_X_POS
player_y = CHAR_Y_POS
player_x_change = 0
player_y_change = 0
enemyimg =[]
enemy_x =[]
enemy_y =[]
enemy_x_change =[]
enemy_y_change =[]
num_enemies = 5
for i in range(num_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0, SCREEN_WIDTH - 64))
    enemy_y.append(random.randint(ENEMYSTART_Y_MIN, ENEMYSTART_Y_MAX))
    enemy_x_change.append(ENEMYX_SPEED)
    enemy_y_change.append(ENEMYY_SPEED)
bulletimg = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = CHAR_Y_POS
bullet_x_change = 0
bullet_y_change = BULLET_SPEED
bullet_state = "ready"
score = 0
font= pygame.font.Font('freesansbold.ttf',36)
text_x=650
text_y=10
game_over_font = pygame.font.Font('freesansbold.ttf', 48)
def show_score(x,y):
    display_score=font.render("score:"+str(score),True,(255,255,255))
    screen.blit(display_score,(x,y))
def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text,(300, 250))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x + 16,y + 10))
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance=math.sqrt(((enemy_x - bullet_x)**2) + ((enemy_y - bullet_y)**2))
    return distance < COLLISION_DISTANCE
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(icon,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key==pygame.K_LEFT:
                player_x_change =-5
            if event.key==pygame.K_RIGHT:
                player_x_change =5
            if event.key==pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            player_x_change = 0
    player_x += player_x_change
    player_x =max(0, min(player_x, SCREEN_WIDTH - 64))
    for i in range(num_enemies):
        if enemy_y [i]>600:
            for j in range(num_enemies):
               enemy_y[j]=2000
            game_over_text()
            break
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <=0 or enemy_x[i] >= SCREEN_WIDTH - 64:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]
        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = CHAR_Y_POS
            bullet_state = "ready"
            score += 1
            enemy_x[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemy_y[i] = random.randint(ENEMYSTART_Y_MIN, ENEMYSTART_Y_MAX)
        enemy(enemy_x[i], enemy_y[i], i)
    if bullet_y <=0:
        bullet_y = CHAR_Y_POS
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()