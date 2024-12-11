import pygame
from utils import *

GROUND = pygame.image.load("dirt_floor.jpg")
WIDTH, HEIGHT = GROUND.get_width(), GROUND.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

MAZE = scale_image(pygame.image.load("mazes/stone_maze1.png"),1)

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    WIN.blit(GROUND,(0, 0))
    WIN.blit(MAZE,(170, 100))

    pygame.display.update()

pygame.quit()
