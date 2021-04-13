import pygame, sys
from ball import Ball
from pad import Pad

pygame.init()

screen_size = width, height = 800, 600
screen_color = (80, 160, 240)
ball_radius = 10
pad_width = 10
pad_height = 100

screen = pygame.display.set_mode(screen_size)
ball = Ball((width / 2) - ball_radius / 2, (height / 2) - ball_radius / 2, ball_radius, 0)
player = Pad(10, (height / 2) - 50, pad_width, pad_height, 0)
computer = Pad(width - 20, (height / 2) - 50, pad_width, pad_height, 0)

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

    ball.update(screen_size)
    player.update(screen_size)
    screen.fill(screen_color)
    screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    screen.blit(computer.image, computer.rect)
    pygame.display.flip()