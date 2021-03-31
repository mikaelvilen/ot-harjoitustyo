import pygame, sys

size = width, height = 800, 600
print(size)
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((90, 160, 240))
    pygame.display.flip()