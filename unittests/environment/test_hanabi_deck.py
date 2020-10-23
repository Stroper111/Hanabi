import unittest
from itertools import product

from environment.constants import Colors, Rank

from environment import HanabiCard, HanabiDeck


class TestHanabiCard(unittest.TestCase):
    def test_colors(self):
        for color, rank in product(Colors, Rank):
            card = HanabiCard(color, rank)
            print(card, end=' ')


class TestHanabiDeck(unittest.TestCase):
    def test_deck(self):
        deck = HanabiDeck()
        deck.render()
        self.assertEqual(60, len(deck._cards), "Wrong number of cards for 6 colors")

        deck = HanabiDeck(colors=[color for color in Colors if color.value != 'M'])
        deck.render()
        self.assertEqual(50, len(deck._cards), "Wrong number of cards for 5 colors")

    def test_deck_pointer(self):
        deck = HanabiDeck()
        init, _ = deck.render()
        deck._pointer = 25

        remaining, played = deck.render()
        deck.render()

        self.assertEqual(25, len(played), f"Number of played is not consistent with deck pointer.")

    def test_hand_cards(self):
        deck = HanabiDeck()
        for hand_size in range(1, 6):
            cards = deck.provide_hand(hand_size=hand_size)
            self.assertEqual(hand_size, len(cards))

    def test_empty(self):
        deck = HanabiDeck()
        cards_drawn = 0
        while not deck.empty:
            deck.draw()
            cards_drawn += 1
        self.assertEqual(60, cards_drawn, "The number of drawn cards is not equal to the deck size.")

    def test_remaining(self):
        deck = HanabiDeck()
        for remaining in reversed(range(60)):
            deck.draw()
            self.assertEqual(remaining, deck.remaining, "The number of drawn cards is not equal to the deck size.")

    def test_empty_with_player_hands(self):
        deck = HanabiDeck()
        deck.provide_hand(hand_size=5)
        for remaining in reversed(range(55)):
            deck.draw()
            self.assertEqual(remaining, deck.remaining, "The number of drawn cards is not equal to the deck size.")


if __name__ == '__main__':
    unittest.main()
