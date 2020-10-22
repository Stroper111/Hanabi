import random

from environment import HanabiDeck, HanabiPlayer
from environment.constants import Colors


class Hanabi:

    def __init__(self, agents: list, hand_size=None, number_of_colors=5):
        assert 2 <= len(agents) <= 5, f"Requires 2-5 players, you entered {len(agents)}."

        self.agents = agents
        self.hand_size = hand_size if hand_size is not None else 5 if len(agents) <= 3 else 4
        self.colors = [color for idx, color in enumerate(Colors) if idx < number_of_colors]

        self.deck = HanabiDeck(colors=self.colors)
        self.players = [HanabiPlayer(idx, self.deck.provide_hand(hand_size)) for idx in range(len(agents))]
        self.counter = 8
        self.info = dict(hints=8, fuses=0, players=len(self.players), current_player=random.randint(0, len(agents) - 1))

    def render(self):
        print(f"General information:"
              f"\n\t- Current player: {self.info['current_player']}"
              f"\n\t- Hint tokens: {self.info['hints']}"
              f"\n\t- Fuse tokens: {self.info['fuses']}"
              f"\n\t- Cards remaining: {self.deck.remaining}")
        [player.render() for player in self.players if player.id != self.info['current_player']]

    def action(self, action):
        pass
