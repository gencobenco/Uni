class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def update_board(self, row, col, player):
        if self.board[row][col] == " ":
            self.board[row][col] = player
            return True
        return False

    def is_full(self):
        return all(all(cell != " " for cell in row) for row in self.board)


class Player:
    def __init__(self, symbol):
        self.symbol = symbol


class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.current_player = 0

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def check_winner(self):
        b = self.board.board

        # Check rows, columns, and diagonals
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != " " or b[0][i] == b[1][i] == b[2][i] != " ":
                return True
        if b[0][0] == b[1][1] == b[2][2] != " " or b[0][2] == b[1][1] == b[2][0] != " ":
            return True
        return False

    def play_game(self):
        while True:
            self.board.display()
            row = int(input(f"Player {self.players[self.current_player].symbol}, enter row: "))
            col = int(input(f"Player {self.players[self.current_player].symbol}, enter column: "))

            if not self.board.update_board(row, col, self.players[self.current_player].symbol):
                print("Invalid move, try again.")
                continue

            if self.check_winner():
                self.board.display()
                print(f"Player {self.players[self.current_player].symbol} wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("It's a tie!")
                break

            self.switch_player()

game = TicTacToe()
# game.play_game()

from enum import Enum, auto

WINNING_LOCATIONS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

class Player:
    X = auto()
    O = auto()

class Game:
    def __init__(self, board=None):
        self.board = Board() if board is None else board
            
    def is_over(self):
        # return True if game over, else False
        pass

    def get_winner(self):
        # return winning player or None
        pass

    def play(self):
        # play with user interaction
        pass

class Board:
    def __init__(self, bx=None, bo=None):
        bx = set() if bx is None else set(bx)
        bo = set() if bo is None else set(bo)
        self.marks = {Player.X: bx, Player.O: bo}

    def free_slots(self):
        # return free slots
        pass

    def make_move(self, player, position):
        # make move
        pass
        
    def is_valid_move(self, move):
        # return True if a move is allowed, else False
        pass
        
    def display(self):
        # print the board,
        # output should look like:
        # X O _
        # O _ X
        # _ _ X
        pass

Game()