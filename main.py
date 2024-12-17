import pygame
from utils import *

GROUND = pygame.image.load("dirt_floor.jpg")
WIDTH, HEIGHT = GROUND.get_width(), GROUND.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

MAZE = scale_image(pygame.image.load("mazes/stone_maze1.png"),1.7)
DEF_CHAR = scale_image(pygame.image.load("def_char/da_idle1.png"),0.5)

IDLE_FRAMES = [scale_image(pygame.image.load(f"def_char/da_idle{i}.png"), 0.5) for i in range(1, 5)]


run = True
clock = pygame.time.Clock()

class Sprites:
    def __init__(self,max_vel,acceleration):
        self.max_vel = max_vel
        self.acceleration = acceleration
        self.x,self.y = self.START_POS
        self.velocity_y = 0  # Track vertical velocity



    # def walk_down(self):
    #     self.y += self.acceleration


class Character(Sprites):
    IMG = DEF_CHAR
    START_POS = (210, 200)

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))
    def walk_down(self, moving):
        if moving:
            if self.velocity_y <= self.max_vel:
                self.velocity_y += self.acceleration
            else:
                self.velocity_y = self.max_vel
            self.y += self.velocity_y






character = Character(6,0.5)

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break


    WIN.blit(GROUND,(0, 0))
    WIN.blit(MAZE,(130, 130))
    keys = pygame.key.get_pressed()
    character.walk_down(keys[pygame.K_DOWN])
    character.draw(WIN)


    pygame.display.update()

pygame.quit()
