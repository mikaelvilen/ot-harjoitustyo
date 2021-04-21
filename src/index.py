import sys
import pygame
from ball import Ball
from pad import Pad
from game_loop import Gameloop

pygame.init()

SCREEN_SIZE = width, height = 800, 600
SCREEN_COLOR = (80, 160, 240)
BALL_RADIUS = 10
PAD_WIDTH = 10
PAD_HEIGHT = 100

screen = pygame.display.set_mode(SCREEN_SIZE)
ball = Ball((width / 2) - BALL_RADIUS / 2, (height / 2) -
            BALL_RADIUS / 2, BALL_RADIUS, 0, 0)
player = Pad(0, (height / 2) - 50, PAD_WIDTH, PAD_HEIGHT, 0)
computer = Pad(width - 10, (height / 2) - 50, PAD_WIDTH, PAD_HEIGHT, 0)

game_loop = Gameloop(screen, SCREEN_SIZE, SCREEN_COLOR, player, computer, ball)

game_loop.start()
