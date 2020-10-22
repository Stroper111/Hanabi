import random

from itertools import product
from colorama import Fore, Style

from environment.constants import Colors, Rank


class HanabiCard:
    def __init__(self, color: Colors, rank: Rank):
        self._color = color
        self._rank = rank
        self._text = self.colored(text=f"{self._color.get(self._color)}{self.rank.value}", color=self._color.name)

    def __str__(self):
        return self._text

    def __repr__(self):
        return f"<class {type(self).__name__}, ({self._text})>"

    @property
    def color(self):
        return self._color

    @property
    def rank(self):
        return self._rank

    @staticmethod
    def colored(text, color):
        return getattr(Fore, color) + Style.BRIGHT + text + Style.RESET_ALL


class HanabiDeck:
    ranks = (Rank.ONE, Rank.ONE, Rank.ONE, Rank.TWO, Rank.TWO, Rank.THREE, Rank.THREE, Rank.FOUR, Rank.FOUR, Rank.FIVE)

    def __init__(self, colors=Colors):
        self._cards = list(product(colors, self.ranks))
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

    def render(self):
        remaining = list(map(str, self._deck[self._pointer:]))
        played = list(map(str, self._deck[:self._pointer]))
        print(f"Deck:\n\t- Remaining: {' '.join(remaining)}\n\t- Played   : {' '.join(played)}")
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
