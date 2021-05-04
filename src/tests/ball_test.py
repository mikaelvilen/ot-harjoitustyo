import unittest
from sprites.ball import Ball
from sprites.pad import Pad


class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(400, 300, 10, 2, 2)
        self.pad = Pad(0, 0, 10, 100, 0)
        self.screen_size = (800, 600)

    def test_ball_collides_with_top_and_bottom_walls(self):
        self.ball.rect.y = 601
        top = self.ball.check_collision_walls(self.screen_size)
        self.ball.rect.y = -1
        bottom = self.ball.check_collision_walls(self.screen_size)
        self.assertEqual((top, bottom), (2, 2))

    def test_ball_collides_with_pads(self):
        self.ball.rect.x = 0
        self.ball.rect.y = 0
        self.assertEqual(self.ball.check_collision_pad(
            self.pad, self.pad), 1)
