import pygame
import os
from utils import *

GROUND = pygame.image.load("dirt_floor.jpg")
WIDTH, HEIGHT = GROUND.get_width(), GROUND.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

MAZE = scale_image(pygame.image.load("mazes/stone_maze1.png"),1.7)
DEF_CHAR = "def_char"




class Sprites:
    def __init__(self,max_vel,acceleration):
        self.max_vel = max_vel
        self.acceleration = acceleration
        self.x,self.y = self.START_POS
        self.velocity_y = 0  # Track vertical velocity





class Character(Sprites):
    IMG = scale_image(pygame.image.load(f"{DEF_CHAR}/da_idle1.png"),0.5)
    START_POS = (210, 200)

    def __init__(self, max_vel, acceleration):
        super().__init__(max_vel, acceleration)
        self.image_folder = DEF_CHAR
        self.frame_count = 5
        self.frames = []
        self.current_frame = 1
        self.frame_delay = 100
        self.last_update = pygame.time.get_ticks()
        self.is_moving = False

        for i in range(1, self.frame_count):
            frame_path = os.path.join(self.image_folder, f"da_idle{i}.png")
            frame = scale_image(pygame.image.load(frame_path),0.5)
            self.frames.append(frame)

    def draw(self, win):
        current_img = self.frames[self.current_frame]

        # Center the frame on the character's position
        frame_rect = current_img.get_rect(center=(self.x, self.y))

        # Blit the current frame
        win.blit(current_img, frame_rect.topleft)
    def walk_down(self, moving):
        if moving:
            self.is_moving = True
            if self.velocity_y <= self.max_vel:
                self.velocity_y += self.acceleration
            else:
                self.velocity_y = self.max_vel
            self.y += self.velocity_y
        else:
            self.is_moving = False

    def update_animation(self):
        if self.is_moving is False:
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_delay:
                self.current_frame = (self.current_frame + 1) % len(self.frames)  # Loop back to the first frame
                self.last_update = now













character = Character(6,0.5)

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break



    keys = pygame.key.get_pressed()
    character.walk_down(keys[pygame.K_DOWN])


    character.update_animation()
    WIN.blit(GROUND, (0, 0))
    WIN.blit(MAZE, (130, 130))

    character.draw(WIN)


    pygame.display.update()

pygame.quit()
