import unittest
import pygame
from game_loop import Gameloop
from sprites.ball import Ball
from sprites.pad import Pad
from screen import Screen

SCREEN_SIZE = width, height = 800, 600
SCREEN_COLOR = (80, 160, 240)
BALL_RADIUS = 10
PAD_WIDTH = 10
PAD_HEIGHT = 50

class TestGameloop(unittest.TestCase):
    def setUp(self):
        self.font = None
        self.player = Pad(0, (height / 2) - 50, PAD_WIDTH, PAD_HEIGHT, 0)
        self.computer = Pad(width - 10, (height / 2) - 50, PAD_WIDTH, PAD_HEIGHT, 0)
        self.ball = Ball((width / 2) - BALL_RADIUS / 2, (height / 2) -
            BALL_RADIUS / 2, BALL_RADIUS, 0, 0)
        self.screen = Screen(width, height, SCREEN_COLOR, self.font)
        self.py_display = pygame.display.set_mode(SCREEN_SIZE)
        self.game_loop = Gameloop(self.screen, self.py_display, self.player, self.computer, self.ball)
        self.score = 0
        self.game_active = False

    def test_test(self):
        self.assertEqual(True, True)
