import unittest
import pygame
from pygame.locals import *
from game_loop import Gameloop
from sprites.ball import Ball
from sprites.pad import Pad
from screen import Screen

SCREEN_SIZE = width, height = 800, 600
SCREEN_COLOR = (80, 160, 240)
BALL_RADIUS = 10
PAD_WIDTH = 10
PAD_HEIGHT = 50
pygame.init()

class TestGameloop(unittest.TestCase):
    def setUp(self):
        self.player = Pad(0, (height / 2) - 50, PAD_WIDTH, PAD_HEIGHT, 0)
        self.computer = Pad(width - 10, (height / 2) - 50, PAD_WIDTH, PAD_HEIGHT, 0)
        self.ball = Ball((width / 2) - BALL_RADIUS / 2, (height / 2) -
            BALL_RADIUS / 2, BALL_RADIUS, 0, 0)
        self.font = pygame.font.Font('src/assets/8bitOperatorPlus-Regular.ttf', 16)
        self.screen = Screen(width, height, SCREEN_COLOR, self.font, self.font)
        self.py_display = pygame.display.set_mode(SCREEN_SIZE)
        self.game_loop = Gameloop(self.screen, self.py_display, self.player, self.computer, self.ball)
        self.score = 0
        self.game_active = False

    def test_game_starts_on_key_press(self):
        event = pygame.event.Event(KEYDOWN, key=13)
        pygame.event.post(event)
        self.game_loop._handle_events()
        self.assertEqual(self.ball.velocity, [10, 10])

    def test_pad_moves_with_arrow_key_down(self):
        event = pygame.event.Event(KEYDOWN, key=K_UP)
        pygame.event.post(event)
        self.game_loop._handle_events()
        self.assertEqual(self.player.velocity, -10)

    def test_pad_stops_with_arrow_key_up(self):
        event = pygame.event.Event(KEYUP, key=K_UP)
        pygame.event.post(event)
        self.game_loop._handle_events()
        self.assertEqual(self.player.velocity, 0)

    def test_game_ends_on_end_wall_collision(self):
        event = pygame.event.Event(KEYDOWN, key=13)
        pygame.event.post(event)
        self.game_loop._handle_events()
        self.ball.rect.x = -1
        self.game_loop._handle_collisions()
        self.assertEqual(self.ball.velocity, [0, 0])

    def test_ball_centers(self):
        self.ball.rect.x = -1
        self.game_loop._handle_collisions()
        self.assertEqual(self.ball.rect.x, 395)

    def test_ball_changes_direction_and_speeds_up_on_collisions_with_pads(self):
        event = pygame.event.Event(KEYDOWN, key=13)
        pygame.event.post(event)
        self.game_loop._handle_events()
        self.ball.rect.x = 0
        self.ball.rect.y = self.player.rect.y
        self.game_loop._handle_collisions()
        self.assertEqual(self.ball.velocity, [-10.1, 10.1])

