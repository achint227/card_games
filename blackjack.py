from deck import Deck


class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0

    def __repr__(self) -> str:
        return ",".join([str(card) for card in self.cards]) + f"->{self.score}"

    def draw(self, deck):
        card = deck.draw()
        if card.rank == "A":
            if self.score + 11 > 21:
                self.score += 1
            else:
                self.score += 11
        elif card.rank in "JQK":
            self.score += 10

        else:
            self.score += int(card.rank)
        self.cards.append(card)

    def check_blackjack(self):
        return (
            len(self.cards) == 2
            and any([card.rank == "A" for card in self.cards])
            and any([card.rank == "J" for card in self.cards])
        )


def new_game(bet=1000):
    dealer = Hand()
    player = Hand()
    d = Deck()
    dealer.draw(d)
    player.draw(d)
    dealer.draw(d)
    player.draw(d)
    print(f"Dealer: {dealer}")
    print(f"Player: {player}")

    def check_blackjack():
        if dealer.score == 21:
            if player.score == 21:
                if player.check_blackjack() and dealer.check_blackjack():
                    print("DRAW")
                    return True
                elif dealer.check_blackjack():
                    print("BLACKJACK! YOU LOST")
                    return True
        elif player.check_blackjack():
            print("BLACKJACK! YOU WON")
            return True

    def check_win():
        if check_busted():
            return
        if dealer.score < player.score <= 21:
            print("YOU WON")
            return True
        elif player.score < dealer.score <= 21:
            print("YOU LOST")
            return False
        else:
            print("DRAW")
            return False

    def check_busted(p=True):
        if dealer.score > 21 and player.score <= 21:
            if p:
                print("DEALER BUSTED")
            return True

        if player.score > 21 and dealer.score <= 21:
            if p:
                print("PLAYER BUSTED")
            return True

    check_busted()
    if check_blackjack():
        return
    choice = "h"
    while dealer.score < 17 or choice in ["HIT", "H", "hit", "h"]:
        if check_busted():
            return
        if choice not in ["HIT", "H", "hit", "h"]:
            break
        if player.score >= 21 and dealer.score>=17:
            break
        if dealer.score < 17:
            dealer.draw(d)
        choice = input("Hit or Stand?:")
        if choice in ["HIT", "H", "hit", "h"]:
            player.draw(d)
        print(f"Dealer: {dealer}")
        print(f"Player: {player}")
        if dealer.score < 17:
            continue
    check_win()


if __name__ == "__main__":
    choice = "y"
    while choice in "yY":
        new_game()
        choice = input("New Game? (Y/N):")
