import pygame
from ball import Ball
from pad import Pad
from game_loop import Gameloop
from screen import Screen


pygame.init()

SCREEN_SIZE = width, height = 800, 600
SCREEN_COLOR = (80, 160, 240)
FONT = pygame.font.Font(
            'src/assets/8bitOperatorPlus-Regular.ttf', 30)
BALL_RADIUS = 10
PAD_WIDTH = 10
PAD_HEIGHT = 50

screen = Screen(width, height, SCREEN_COLOR, FONT)
py_display = pygame.display.set_mode(screen.size)
ball = Ball((width / 2) - BALL_RADIUS / 2, (height / 2) -
            BALL_RADIUS / 2, BALL_RADIUS, 0, 0)
player = Pad(0, (height / 2) - 50, PAD_WIDTH, PAD_HEIGHT, 0)
computer = Pad(width - 10, (height / 2) - 50, PAD_WIDTH, PAD_HEIGHT, 0)
game_loop = Gameloop(screen, py_display, player, computer, ball)

game_loop.start()
