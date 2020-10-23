import random

from itertools import product
from typing import List

from environment.utils.ansi import Fore, Style
from environment.utils.constants import Colors, Rank


class HanabiCard:
    def __init__(self, color: Colors, rank: Rank):
        self._color = color
        self._rank = rank
        self._text = self.colored(text=f"{self.color}{self.rank}", color=self._color.name)

    def __str__(self):
        return self._text

    def __repr__(self):
        return f"<class {type(self).__name__}, ({self._text})>"

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._text == other._text
        return False

    @property
    def color(self):
        return self._color.value

    @property
    def rank(self):
        return self._rank.value

    @property
    def index(self):
        return self._color.index

    @staticmethod
    def colored(text, color):
        return getattr(Fore, color) + Style.BRIGHT + text + Style.RESET_ALL


class HanabiDeck:
    ranks = (Rank.ONE, Rank.ONE, Rank.ONE, Rank.TWO, Rank.TWO, Rank.THREE, Rank.THREE, Rank.FOUR, Rank.FOUR, Rank.FIVE)

    def __init__(self, colors=None, ranks: List[Rank] = None):
        self._colors = Colors.normal() if colors is None else [color for color in colors if color != Colors.UNKNOWN]
        self._ranks = ranks if ranks is not None else self.ranks
        self._cards = list(product(self._colors, self._ranks))
        self._deck = self._create_random_deck()
        self._pointer = 0

    def __repr__(self):
        return f"<class {type(self).__name__},  (size={len(self._deck)})>"

    @property
    def empty(self):
        return self._pointer >= len(self._deck)

    @property
    def remaining(self):
        return len(self._deck) - self._pointer

    def _create_random_deck(self):
        deck = [HanabiCard(color, rank) for color, rank in self._cards]
        random.shuffle(deck)
        return deck

    def reset(self):
        """ Reset the deck for a new game.  """
        self._deck = self._create_random_deck()
        self._pointer = 0

    def render(self):
        remaining = list(map(str, self._deck[self._pointer:]))
        played = list(map(str, self._deck[:self._pointer]))
        print(f"\nDeck:\n\t- Remaining: {' '.join(remaining)}\n\t- Played   : {' '.join(played)}")
        return remaining, played

    def provide_hand(self, hand_size=5):
        hand_cards = self._deck[self._pointer: self._pointer + hand_size]
        self._pointer += hand_size
        return hand_cards

    def draw(self):
        """ Draw a single card from the deck.  """
        card = self._deck[self._pointer]
        self._pointer += 1
        return card
