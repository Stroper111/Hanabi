from environment import Hanabi
from environment.utils.constants import Actions

if __name__ == '__main__':
    env = Hanabi(agents=list('12'), )

    # Run a single game loop
    obs = env.reset()
    done = False
    while not done:
        action = Actions.sample(hand_size=env.hand_size, players=len(env.players), hints=env.hints)
        obs, reward, done, info = env.step(action)
        env.render()

    # Unpack an observations
    for key, value in obs.items():
        if key == 'turns log':
            print(f"Key: {key} (unpacked dict)", end='\n\n')
            for turn, value in value.items():
                print(f"\t - Turn {turn}: {' '.join(map(str, value))}")
            continue
        print(f"Key: {key}\n{value}", end='\n\n')
