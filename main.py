import pygame


GROUND = pygame.image.load("dirt_floor.jpg")
WIDTH, HEIGHT = GROUND.get_width(), GROUND.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    WIN.blit(GROUND,(0, 0))
    pygame.display.update()

pygame.quit()
