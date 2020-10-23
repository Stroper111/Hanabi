import unittest

from environment import Hanabi
from environment.utils.constants import Actions


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
            action = Actions.sample(hand_size=4, players=4, hints=env.info['hints'])
            obs, reward, done, info = env.step(action)

    def test_speed_runs(self):
        env = Hanabi(agents=list('1234'), hand_size=4)
        steps = 0
        for episode in range(1, 1_001):
            done = False
            env.reset()
            reward = 0
            while not done:
                action = Actions.sample(hand_size=4, players=4, hints=env.info['hints'])
                obs, reward, done, info = env.step(action)
                steps += 1
            print(f"\rEpisode: {episode:4d}/1000, steps: {steps:6d}, reward: {reward}", end='')


if __name__ == '__main__':
    unittest.main()
