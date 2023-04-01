import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

player_img = pygame.image.load('player.png')

player_x = 400
player_y = 500
player_speed = 5

enemy_img = pygame.image.load('enemy.png')
enemy_x = random.randint(0, 800)
enemy_y = random.randint(50, 150)
enemy_speed = 2

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def draw_player():
  screen.blit(player_img, (player_x, player_y))

def draw_enemy():
  screen.blit(enemy_img, (enemy_x, enemy_y))

def move_enemy():
  global enemy_x, enemy_y
  enemy_y += enemy_speed
  if enemy_y > 600:
    enemy_x = random.randint(0, 800)
    enemy_y = random.randint(50, 150)

def collision_detection():
  global score
  distance = ((player_x-enemy_x)**2 + (player_y-enemy_y)**2)**0.5
  if distance < 50:
    enemy_x = random.randint(0, 800)
    enemy_y = random.randint(50, 150)
    score += 1

def draw_score():
  score_text = font.render('Score: ' + str(score), True, (255, 255, 255))
  screen.blit(score_text, (10, 10))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    player_x -= player_speed
  if keys[pygame.K_RIGHT]:
    player_x += player_speed
  if keys[pygame.K_UP]:
    player_y -= player_speed
  if keys[pygame.K_DOWN]:
    player_y += player_speed


  move_enemy()
  collision_detection()

  screen.fill((0, 0, 0))
  draw_player()
  draw_enemy()
  draw_score()
  pygame.display.update()

  clock.tick(60)

pygame.quit()
