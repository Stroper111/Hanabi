import unittest

from environment import Hanabi


class TestHanabi(unittest.TestCase):
    def test_init(self):
        env = Hanabi(agents=list('1234'), hand_size=4)
        env.render()


if __name__ == '__main__':
    unittest.main()
