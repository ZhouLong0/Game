import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((600, 750))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

test_surface = pygame.image.load("./graphics/background_space.png")
plane_surface = pygame.image.load("./graphics/plane.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw all our elements
    # update everything

    screen.blit(test_surface, (0, 0))
    screen.blit(plane_surface, (270, 600))

    pygame.display.update()
    clock.tick(60)  # don't want our game run faster that 60 framerate per second
