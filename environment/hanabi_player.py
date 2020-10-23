from typing import List

from environment.constants import Colors, Rank
from environment import HanabiCard


class HanabiPlayer:
    def __init__(self, player_id: int, cards: List[HanabiCard]):
        self.id = player_id
        self._hand = cards
        self._info = [('?', '?') for _ in range(len(cards))]

    def render(self, can_see=True):
        """
            Displays the player hand to the console.

        :param can_see: boolean
            If True the player cards are shown, otherwise the cards are hidden.
        """
        print(f"\nPlayer: {self.id}")
        for card, (color, rank) in zip(self._hand, self._info):
            print(f"\t{str(card)} || {color}{rank}") if can_see else print(f"\t?? || {color}{rank}")

    def play(self, index):
        """ PLay a card from the player hand.  (similar to discard)  """
        self._info.pop(index)
        return self._hand.pop(index)

    def discard(self, index):
        """ Remove a card from the player hand. (similar to play)  """
        self._info.pop(index)
        return self._hand.pop(index)

    def inform_color(self, info_color: Colors):
        """ Update the player information with the color information.  """
        info = []
        for card, (color, rank) in zip(self._hand, self._info):
            if card.color == info_color.name[0]:
                color = info_color.get(info_color)
            info.append((color, rank))
        self._info = info

    def inform_rank(self, info_rank: int):
        """ Update the player information with the rank information.  """
        info = []
        for card, (color, rank) in zip(self._hand, self._info):
            if card.rank.value == info_rank:
                rank = info_rank
            info.append((color, rank))
        self._info = info

    def add_card(self, card):
        """ Add a new card to the player hand.   """
        self._hand.insert(0, card)
        self._info.insert(0, ('?', '?'))
