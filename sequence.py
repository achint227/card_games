from collections import defaultdict
from deck import Deck




class Sequence:
    def __init__(self):
        self.board = [["*" for _ in range(10)] for _ in range(10)]
        self.mapping = defaultdict(list)
        self.create_board()

    def place_token(self, r, c, t):
        self.board[r][c] = t

    def display_board(self):
        print("-" * 38)

        for row in self.board:
            print("|".join([f"{str(_):^3}" for _ in row]))
            print("-" * 38)

    def create_board(self):
        left, right, top, bottom = 0, 9, 0, 9

# Fill the board spirally from top-left to bottom-right
        deck = Deck(False, True)
        while left <= right:
            for c in range(left, right + 1):
                if (top, c) in [(0, 0), (0, 9)]:
                    continue
                if not deck.is_empty():
                    card = deck.draw()
                    self.mapping[str(card)].append((top, c))
                    # self.board[top][c] = card
            top += 1
            # fill right col
            for r in range(top, bottom + 1):
                if (r, right) == (9, 9):
                    continue

                if not deck.is_empty():
                    card = deck.draw()
                    self.mapping[str(card)].append((r, right))
                    # self.board[r][right] = card
            right -= 1
            # fill bot row in rev
            for c in range(right, left - 1, -1):
                if (bottom, c) == (9, 0):
                    continue
                if not deck.is_empty():
                    card = deck.draw()
                    self.mapping[str(card)].append((bottom, c))
                    # self.board[bottom][c] = card
            bottom -= 1

            # fill left col in rev
            for r in range(bottom, top - 1, -1):
                if not deck.is_empty():
                    card = deck.draw()
                    self.mapping[str(card)].append((r, left))
                    # self.board[r][left] = card
            left += 1

    def get_valid_squares(self, card):
        return [(r, c) for (r, c) in self.mapping[str(card)] if self.board[r][c] == "*"]

    def remove_token(self, r, c):
        self.board[r][c] = "."


if __name__ == "__main__":
    game = Sequence()
    game.place_token(4,9,"X")
    game.display_board()
    print(game.get_valid_squares("♠A"))
