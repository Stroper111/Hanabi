import unittest

from environment import HanabiPlayer, HanabiDeck, HanabiCard
from environment.constants import Rank, Colors


class TestHanabiPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.deck = HanabiDeck(ranks=[Rank.ONE])
        self.cards = self.deck.provide_hand(hand_size=6)

    def test_init(self):
        player = HanabiPlayer(player_id=0, cards=self.cards)
        player.render()

    def test_info_hidden(self):
        player = HanabiPlayer(player_id=0, cards=self.cards)
        player.render(can_see=False)

    def test_info_color(self):
        player = HanabiPlayer(player_id=0, cards=self.cards)
        player.inform_color(Colors.BLACK)
        player.render()

    def test_info_rank(self):
        player = HanabiPlayer(player_id=0, cards=self.cards)
        player.inform_rank(Rank.ONE.value)
        player.render()

    def test_play(self):
        player = HanabiPlayer(player_id=0, cards=self.cards)
        card = player.play(3)
        player.render()
        self.assertEqual(5, len(player._hand), f"Player didn't properly play a card.")
        self.assertEqual(True, isinstance(card, HanabiCard), f"return value from play isn't a card.")

    def test_discard(self):
        player = HanabiPlayer(player_id=0, cards=self.cards)
        card = player.discard(3)
        player.render()
        self.assertEqual(5, len(player._hand), f"Player didn't properly discard a card.")
        self.assertEqual(True, isinstance(card, HanabiCard), f"return value from discard isn't a card.")

    def test_add_card(self):
        player = HanabiPlayer(player_id=0, cards=self.cards)
        player.add_card(HanabiCard(color=Colors.RED, rank=Rank.TWO))
        player.render()
        self.assertEqual(7, len(player._hand), f"Player didn't properly add a new card to his hand.")


if __name__ == '__main__':
    unittest.main()
