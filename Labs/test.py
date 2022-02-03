import pygame
import random
from random import randint
pygame.init()

screen = pygame.display.set_mode((500,750)) 
#background = pygame.image.load('cityscape python.jpg')


Bird = pygame.image.load('bird.png')
bird_x = 50
bird_y = 300
bird_y_change = 0

def display_bird(x,y):
  screen.blit(Bird, (x,y))


Obstacle_Width = 70
Obstacle_Height = random.randint(150,450)
Obstacle_Colour = (221, 253, 117)
Obstacle_X_Change = -4
obstacle_x = 500
bottom_obstacle_height = 0

def display_obstacle(height):
  pygame.draw.rect(screen, Obstacle_Colour, (obstacle_x, 0, Obstacle_Width, height))
  botton_obstacle_heiht = 635 - height - 158
  pygame.draw.rect(screen, Obstacle_Colour, (obstacle_x, 635, Obstacle_Width, -bottom_obstacle_height))


def collision_detection (obstacle_x, Obstacle_Height, bird_y, bottom_obstacle_height):
  if obstacle_x >= 50 and obstacle_x <= (50 + 64):
    if bird_y <= Obstacle_Height or bird_y >= (bottom_obstacle_height - 64):
      return True
  return False

score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)

def score_display(score):
  display = score_font.render(f"score: {score}", True, (255,255,255))

Running = True

while Running:

  screen.fill((0,0,0))
 #line 50 displays the background image.
  screen.blit(background,(0,0))
  for event in pygame.event.get():
    #if event.type == pygame.QUIT:
      #Running = False
    #change by -6.
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        bird_y_change = -6

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_SPACE:
        bird_y_change = -3  


  bird_y += bird_y_change
 
  if bird_y <= 0:
    bird_y = 0
  if bird_y >= 571:
    bird_y = 571

obstacle_x += Obstacle_X_Change
if obstacle_x <= -10:
  obstacle_x = 500
  Obstacle_Height = random.randint(200,400)
display_obstacle(Obstacle_Height )



collision = collision_detection(obstacle_x, Obstacle_Height, bird_y, Obstacle_Height, + 150)

if collision:
  pygame.quit()


display_bird(bird_x, bird_y)


score_display(score)

  

pygame.display.update()

pygame.quit()