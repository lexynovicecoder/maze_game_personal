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
        self.velocity_x = 0




class Character(Sprites):
    IMG = scale_image(pygame.image.load(f"{DEF_CHAR}/da_idle1.png"),0.5)
    START_POS = (210, 200)

    def __init__(self, max_vel, acceleration):
        super().__init__(max_vel, acceleration)
        self.image_folder = DEF_CHAR
        self.idle_frames = self.load_frames("da_idle", 5)
        self.walk_frames = self.load_frames("da_walk", 8)
        self.current_frames = []
        self.current_frame_index = 0
        self.frame_delay = 200
        self.last_update = pygame.time.get_ticks()
        self.is_moving = False

    def load_frames(self, prefix, count):
        """Load animation frames from the given folder."""
        frames = []
        for i in range(1, count + 1):  # Ensure you include the last frame
            frame_path = os.path.join(self.image_folder, f"{prefix}{i}.png")
            frame = scale_image(pygame.image.load(frame_path), 0.5)
            frames.append(frame)

        return frames
    def draw(self, win):
        if not self.current_frames:
            return
        else:
            current_img = self.current_frames[self.current_frame_index]
            win.blit(current_img,(self.x,self.y))



    def navigation(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
            self.is_moving = True
            if keys[pygame.K_DOWN]:
                if self.velocity_y <= self.max_vel:
                    self.velocity_y += self.acceleration
                else:
                    self.velocity_y = self.max_vel
                self.y += self.velocity_y
            if keys[pygame.K_RIGHT]:
                if self.velocity_x <= self.max_vel:
                    self.velocity_x += self.acceleration
                else:
                    self.velocity_x = self.max_vel
                self.x += self.velocity_x



        else:
            self.is_moving = False

    def animation(self):
        now = pygame.time.get_ticks()

        new_frames = self.walk_frames if self.is_moving else self.idle_frames

        # Reset frame index if the animation set changes
        if self.current_frames != new_frames:
            self.current_frames = new_frames
            self.current_frame_index = 0

        if not self.current_frames:
            return
        else:
            if now - self.last_update > self.frame_delay:
               self.current_frame_index = (self.current_frame_index + 1) % len(self.current_frames)
               self.last_update = now








character = Character(6,0.5)

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(55)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break





    character.navigation()
    character.animation()
    WIN.blit(GROUND, (0, 0))
    WIN.blit(MAZE, (130, 130))

    character.draw(WIN)


    pygame.display.update()

pygame.quit()
