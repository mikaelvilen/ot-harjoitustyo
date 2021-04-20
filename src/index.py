import sys
import pygame
from ball import Ball
from pad import Pad

pygame.init()

SCREEN_SIZE = width, height = 800, 600
SCREEN_COLOR = (80, 160, 240)
BALL_RADIUS = 10
PAD_WIDTH = 10
PAD_HEIGHT = 100

screen = pygame.display.set_mode(SCREEN_SIZE)
ball = Ball((width / 2) - BALL_RADIUS / 2, (height / 2) -
            BALL_RADIUS / 2, BALL_RADIUS, -1, -1)
player = Pad(0, (height / 2) - 50, PAD_WIDTH, PAD_HEIGHT, 0)
computer = Pad(width - 10, (height / 2) - 50, PAD_WIDTH, PAD_HEIGHT, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.velocity = -2
            if event.key == pygame.K_DOWN:
                player.velocity = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.velocity = 0
            if event.key == pygame.K_DOWN:
                player.velocity = 0

    if ball.check_collision_pad(player.rect, computer.rect):
        ball.velocity[0] *= -1

    if ball.check_collision_walls(SCREEN_SIZE) != 0:
        if ball.check_collision_walls(SCREEN_SIZE) == 1:
            ball.rect.x = width / 2
            ball.rect.y = height / 2
        if ball.check_collision_walls(SCREEN_SIZE) == 2:
            ball.velocity[1] *= -1
        if ball.check_collision_walls(SCREEN_SIZE) == 3:
            pass

    computer.rect.y = ball.rect.y

    ball.update()
    player.update(SCREEN_SIZE)
    computer.update(SCREEN_SIZE)
    screen.fill(SCREEN_COLOR)
    screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    screen.blit(computer.image, computer.rect)
    pygame.display.flip()
