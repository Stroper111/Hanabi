from enum import Enum
from colorama import Fore, Style

COLOR_STRING = ['RGBWYM']


class Colors(Enum):
    RED = 0
    GREEN = 1
    LIGHTBLUE_EX = 2
    BLACK = 3
    LIGHTYELLOW_EX = 4
    MAGENTA = 5

    def get(self, color: 'Colors'):
        return getattr(Fore, color.name) + Style.BRIGHT + color.value + Style.RESET_ALL


class Rank(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    def get(self, rank: 'Rank'):
        return getattr(Fore, Colors.BLACK.name) + Style.BRIGHT + rank.value + Style.RESET_ALL


class Actions(Enum):
    PLAY = 0
    INFORM_COLOR = 1
    INFORM_RANK = 2
    DISCARD = 3
