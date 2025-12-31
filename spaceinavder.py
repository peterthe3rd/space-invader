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
icon =pygame.image.load("R.jpg")
pygame.display.set_icon(icon)
playerimg = pygame.image.load("R.jpg")
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
    enemyimg.append(pygame.image.load("enemy.jpg"))
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
