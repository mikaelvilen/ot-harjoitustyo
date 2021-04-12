import pygame, sys
from ball import Ball
from pad import Pad

pygame.init()

screen_size = width, height = 800, 600
screen_color = (80, 160, 240)

screen = pygame.display.set_mode(screen_size)
ball = Ball((width / 2) - 5, (height / 2) - 5)
player = Pad(10, (height / 2) - 50, 0)
computer = Pad(width - 20, (height / 2) - 50, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.velocity = -4
            if event.key == pygame.K_DOWN:
                player.velocity = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.velocity = 0
            if event.key == pygame.K_DOWN:
                player.velocity = 0

    ball.rect = ball.rect.move([2, 2])
    player.rect = player.rect.move([0, player.velocity])
    screen.fill(screen_color)
    screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    screen.blit(computer.image, computer.rect)
    pygame.display.flip()