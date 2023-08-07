from collections import deque
import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.suit}{self.rank}"
    
    def __eq__(self, __value: object) -> bool:
        return str(self)==str(__value)


class Deck:
    def __init__(self, shuffle=True, sequence=False):
        self.cards = deque()
        self.create_deck(sequence)
        if shuffle:
            self.shuffle()

    def create_deck(self, sequence):
        suits = ["\u2660", "\u2662", "\u2663", "\u2661"]
        ranks = (
            ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Q", "K", "A"]
            if sequence
            else ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        )
        if sequence:
            for suit in suits[:2]:
                for rank in ranks:
                    self.cards.append(Card(suit, rank))
            for suit in suits[2:]:
                for rank in reversed(ranks):
                    self.cards.append(Card(suit, rank))
            for suit in suits[:2]:
                for rank in ranks:
                    self.cards.append(Card(suit, rank))
            for suit in suits[2:]:
                for rank in reversed(ranks):
                    self.cards.append(Card(suit, rank))
        else:
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.is_empty():
            return self.cards.popleft()
        else:
            raise IndexError("The deck is empty.")

    def is_empty(self):
        return len(self.cards) == 0

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"


if __name__ == "__main__":
    d = Deck()
    print(d)
    for _ in range(7):
        print(d.draw())
    print(d)
