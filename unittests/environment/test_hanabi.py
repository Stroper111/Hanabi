import unittest

from environment import Hanabi
from environment.constants import Actions


class TestHanabi(unittest.TestCase):
    def test_init(self):
        env = Hanabi(agents=list('1234'), hand_size=4)
        env.render()

    def test_action_play(self):
        env = Hanabi(agents=list('1234'), hand_size=4)
        env.render()
        env.step(Actions.PLAY(1, 2))
        env.render()

    def test_action_inform_color(self):
        env = Hanabi(agents=list('1234'), hand_size=4)
        env.render()
        env.step(Actions.INFORM_COLOR(2, 3))
        env.render()

    def test_action_inform_rank(self):
        env = Hanabi(agents=list('1234'), hand_size=4)
        env.render()
        env.step(Actions.INFORM_RANK(2, 3))
        env.render()

    def test_action_discard(self):
        env = Hanabi(agents=list('1234'), hand_size=4)
        env.render()
        env.step(Actions.DISCARD(1))
        env.render()

    def test_action_sample(self):
        env = Hanabi(agents=list('1234'), hand_size=4)
        env.render()
        env.step(Actions.sample(hand_size=4, players=4, hints=env.info['hints']))
        env.render()

    def test_run(self):
        env = Hanabi(agents=list('1234'), hand_size=4)
        done = False
        while not done:
            env.render()
            env.step(Actions.sample(hand_size=4, players=4, hints=env.info['hints']))


if __name__ == '__main__':
    unittest.main()
