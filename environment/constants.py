import random
from enum import Enum
from typing import Tuple

from colorama import Fore, Style

COLOR_STRING = list('RGBWYM?')


class Colors(Enum):
    RED = 'R'
    GREEN = 'G'
    LIGHTBLUE_EX = 'B'
    BLACK = 'W'  # This is more white, than actual White (which is more gray)
    LIGHTYELLOW_EX = 'Y'
    MAGENTA = 'M'
    UNKNOWN = '?'

    @staticmethod
    def normal():
        return Colors.RED, Colors.GREEN, Colors.LIGHTBLUE_EX, Colors.BLACK, Colors.LIGHTYELLOW_EX

    @staticmethod
    def difficult():
        return Colors.RED, Colors.GREEN, Colors.LIGHTBLUE_EX, Colors.BLACK, Colors.LIGHTYELLOW_EX, Colors.MAGENTA

    @property
    def get(self) -> str:
        """ Returns the color value in the right color.  """
        return getattr(Fore, self.name) + Style.BRIGHT + self.value + Style.RESET_ALL

    @property
    def index(self) -> int:
        """ Return the index of a color object.  """
        return COLOR_STRING.index(self.value)

    @staticmethod
    def color(index: int) -> 'Colors':
        """ Return a Colors object, based on an index.  """
        return Colors(COLOR_STRING[index])


class Rank(Enum):
    UNKNOWN = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    @staticmethod
    def get(rank: 'Rank') -> str:
        """ Return the rank in uniform formatting. """
        return getattr(Fore, Colors.BLACK.name) + Style.BRIGHT + rank.value + Style.RESET_ALL


class Actions:
    id: int = None
    index: int = None
    player: int = None

    mapping = {
        0: "Played: {}",
        1: "Inform color: {}, to player: {}",
        2: "Inform rank: {}, to player: {}",
        3: "Discard: {}",
    }

    def __init__(self, action_id, index, player=None):
        self.id = action_id
        self.index = index
        self.player = player

    def __str__(self):
        return f"Actions: (id={self.id}, index={self.index}, player={self.player})"

    def __repr__(self):
        return f"<class {self.__str__()}>"

    @classmethod
    def PLAY(cls, index, *args, **kwargs) -> 'Actions':
        return cls(action_id=0, index=index)

    @classmethod
    def INFORM_COLOR(cls, index, player) -> 'Actions':
        return cls(action_id=1, index=index, player=player)

    @classmethod
    def INFORM_RANK(cls, index, player) -> 'Actions':
        return cls(action_id=2, index=index, player=player)

    @classmethod
    def DISCARD(cls, index, *args, **kwargs) -> 'Actions':
        return cls(action_id=3, index=index)

    @staticmethod
    def sample(hand_size: int, players: int, hints: int) -> 'Actions':
        action = random.choice([Actions.PLAY, Actions.DISCARD])
        if hints:
            action = random.choice([Actions.PLAY, Actions.INFORM_COLOR, Actions.INFORM_RANK, Actions.DISCARD])
        return action(index=random.randint(1, hand_size - 1), player=random.randint(0, players - 1))

    @property
    def humanize(self):
        message = self.mapping.get(self.id)
        message.format((self.index, self.player) if self.player is not None else (self.index,))
        return message

    @property
    def obs(self):
        return self.id, self.index, self.player
