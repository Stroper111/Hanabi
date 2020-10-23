import random
from collections import defaultdict

from environment import HanabiDeck, HanabiPlayer
from environment.constants import Colors, Actions


class Hanabi:

    def __init__(self, agents: list, hand_size=None, number_of_colors=5):
        assert 2 <= len(agents) <= 5, f"Requires 2-5 players, you entered {len(agents)}."

        self.agents = agents
        self.hand_size = hand_size if hand_size is not None else 5 if len(agents) <= 3 else 4
        self.colors = [color for idx, color in enumerate(Colors) if idx <= number_of_colors]

        self.deck = HanabiDeck(colors=self.colors)
        self.players = [HanabiPlayer(idx, self.deck.provide_hand(hand_size)) for idx in range(len(agents))]

        self.log = defaultdict(list)
        self.info = self._create_info()

        self.action_mapping = {
            0: lambda action: self._action_play(action),
            1: lambda action: self._action_inform_color(action),
            2: lambda action: self._action_inform_rank(action),
            3: lambda action: self._action_discard(action),
        }

    def render(self):
        print(f"\n\nGeneral information:"
              f"\n\t- Current player: {self.info['current_player']}"
              f"\n\t- Hint tokens: {self.info['hints']}"
              f"\n\t- Fuse tokens: {self.info['fuses']}"
              f"\n\t- Cards remaining: {self.deck.remaining}")
        [player.render(can_see=player.id != self.info['current_player']) for player in self.players]

    def render_step(self):
        print(f"\nPlayer: {self.info['current_player']}:\n\t-", '\n\t- '.join(self.log[self.info['turns_played']]))

    def step(self, action: Actions):
        """ Action Tuple.  """
        # noinspection PyArgumentList
        obs, reward, done, info = self.action_mapping.get(action.id)(action)
        self.info['turns_played'] += 1
        self.info['current_player'] = (self.info['current_player'] + 1) % len(self.agents)
        return obs, reward, done, info

    def reset(self):
        self.deck.reset()
        self.players = [HanabiPlayer(idx, self.deck.provide_hand(self.hand_size)) for idx in range(len(self.agents))]
        self.log = defaultdict(list)
        self.info = self._create_info()

    def _action_play(self, action):
        player = self.players[self.info['current_player']]
        card = player.play(index=action.index)
        self._handle_play(card)
        self._handle_draw(player)
        return self._handle_returns()

    def _action_inform_color(self, action):
        if self.info['hints'] <= 0:
            raise ValueError(f"There were no hint tokens left, invalid move.")
        self._handle_inform_color(action)
        return self._handle_returns()

    def _action_inform_rank(self, action):
        if self.info['hints'] <= 0:
            raise ValueError(f"There were no hint tokens left, invalid move.")
        self._handle_inform_rank(action)
        return self._handle_returns()

    def _action_discard(self, action):
        player = self.players[self.info['current_player']]
        card = player.discard(index=action.index)
        self._handle_discard(card)
        self._handle_draw(player)
        return self._handle_returns()

    def _handle_play(self, card):
        if self.info['cards_played'][card.color] == card.rank.value - 1:
            self.info['cards_played'][card.color] += 1
            self.log[self.info['turns_played']].append(f"Played card: {card}")
            return True
        self.info['card_discarded'][card.color].append(card.rank.value)
        self.log[self.info['turns_played']].append(f"Tried to play card: {card}, but was not possible")
        return False

    def _handle_discard(self, card):
        self.info['card_discarded'][card.color].append(card.rank.value)
        self.info['fuses'] += 1
        self.log[self.info['turns_played']].append(f"Discard card: {card}")
        return True

    def _handle_inform_color(self, action):
        color = Colors.color(action.index)
        self.players[action.player].inform_color(color)
        self.info['hints'] -= 1
        self.log[self.info['turns_played']].append(f"Informed player: {action.player} of color: {color.get(color)}")
        return True

    def _handle_inform_rank(self, action):
        self.players[action.player].inform_rank(action.index)
        self.info['hints'] -= 1
        self.log[self.info['turns_played']].append(f"Informed player: {action.player} of rank: {action.index}")
        return True

    def _handle_draw(self, player):
        if self.deck.empty:
            self.info['turns_left'] -= 1
            return False
        new_card = self.deck.draw()
        player.add_card(new_card)
        self.log[self.info['turns_played']].append(f"Drew card: {new_card}")
        return True

    def _handle_returns(self):
        done = self.info['turns_left'] <= 0 or self.info['fuses'] >= 3  # TODO add no more valid moves left.
        reward = 0 if not done else sum(self.info['cards_played'].values())
        return self._get_observation(), reward, done, self.info

    def _get_observation(self):
        pass

    def _create_info(self):
        return dict(
                hints=8,
                fuses=0,
                turns_left=len(self.agents) - 1,
                turns_played=0,

                players=len(self.players),
                current_player=random.randint(0, len(self.agents) - 1),

                cards_played={color.name[0]: 0 for color in self.colors},
                card_discarded={color.name[0]: [] for color in self.colors},
        )
