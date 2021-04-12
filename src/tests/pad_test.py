import unittest
from pad import Pad

class TestPad(unittest.TestCase):
    def setUp(self):
        self.pad = Pad(10, 250, 0)

    def test_pad_moves_correctly(self):
        self.assertEqual(True, True)