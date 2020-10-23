from environment import Hanabi
from environment.utils.constants import Actions

if __name__ == '__main__':
    env = Hanabi(agents=list('1234'))
    obs = env.reset()
    done = False
    while not done:
        action = Actions.sample(hand_size=env.hand_size, players=len(env.players), hints=env.hints)
        obs, reward, done, info = env.step(action)
        env.render()
