import unittest
from pad import Pad

class TestPad(unittest.TestCase):
    def setUp(self):
        self.pad = Pad(10, 250, 10, 100, 0)
        self.screen_size = (800, 600)

    def test_pad_stays_on_the_screen(self):
        self.pad.rect.y = -2
        self.pad.update(self.screen_size)
        self.assertEqual(self.pad.rect.y, 0)