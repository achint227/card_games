from collections import defaultdict
from deck import Deck


class Poker:
    def __init__(self):
        self.deck = Deck(shuffle=True)
        self.community = []
        self.players = defaultdict(list)

    def flop(self):
        f = [self.deck.draw() for _ in range(3)]
        self.community.extend(f)

    def turn(self):
        self.community.append(self.deck.draw())

    def river(self):
        self.community.append(self.deck.draw())

    def add_player(self, player_name):
        self.players[player_name] = []

    def distribute_cards(self):
        for player in self.players:
            self.players[player].append(self.deck.draw())
            self.players[player].append(self.deck.draw())

    def __repr__(self) -> str:
        return f"""{self.community[0] if len(self.community)>0 else '*'} {self.community[1] if len(self.community)>1 else '*'} {self.community[2] if len(self.community)>2 else '*'} _ {self.community[3] if len(self.community)>3 else '*'} _ {self.community[4] if len(self.community)>4 else '*'}
{" ".join([f"{player}:{self.players[player]}" for player in self.players]) if len(self.community)>4 else ""}"""

def start_game(players):
    game = Poker()
    for player in players:
        game.add_player(player)
    game.distribute_cards()
    game.flop()
    game.turn()
    game.river()
    print(game)


if __name__ == "__main__":
    players=["Achint","Ayush"]
    start_game(players)