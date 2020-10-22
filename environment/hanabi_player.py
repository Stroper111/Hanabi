from typing import List
from collections import deque

from environment import HanabiCard


class HanabiPlayer:
    def __init__(self, player_id: int, cards: List[HanabiCard]):
        self.id = player_id
        self._hand = cards
        self._info = deque([('?', '?') for _ in range(len(cards))], maxlen=len(cards))

    def render(self):
        print(f"\nPlayer: {self.id}")
        for card, (color, rank) in zip(self._hand, self._info):
            print(f"\t{str(card)} || {color}{rank}")
