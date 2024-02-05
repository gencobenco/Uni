# Funktion zum Erstellen des Spielfelds
def create_board(rows, cols):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    return board

# Funktion zum Anzeigen des Spielfelds
def display_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-" * (4 * len(row) + 1))

# Funktion zum Überprüfen, ob ein Zug gültig ist
def is_valid_move(board, col):
    return board[0][col] == ' '

# Funktion zum Setzen eines Spielsteins
def make_move(board, col, player):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = player
            return

# Funktion zum Überprüfen, ob das Spiel vorbei ist
def is_game_over(board, player):
    for row in board:
        for col in range(len(row) - 3):
            if all([cell == player for cell in row[col:col+4]]):
                return True

    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if all([board[row+i][col] == player for i in range(4)]):
                return True

    for col in range(len(board[0]) - 3):
        for row in range(len(board) - 3):
            if all([board[row+i][col+i] == player for i in range(4)]):
                return True

    for col in range(len(board[0]) - 3):
        for row in range(3, len(board)):
            if all([board[row-i][col+i] == player for i in range(4)]):
                return True

    return False

# Hauptspiel-Funktion
def connect_four():
    rows = 6
    cols = 7
    player = 'X'
    board = create_board(rows, cols)
    turns = 0

    while turns < rows * cols:
        display_board(board)
        col = int(input(f'Spieler {player}, wähle eine Spalte (0-(cols-1): '))
        if 0 <= col < cols and is_valid_move(board, col):
            make_move(board, col, player)
            if is_game_over(board, player):
                display_board(board)
                print(f'Spieler {player} gewinnt!')
                break
            player = 'O' if player == 'X' else 'X'
            turns += 1
        else:
            print('Ungültiger Zug. Versuche es erneut.')

    if turns == rows * cols:
        display_board(board)
        print('Unentschieden!')

if __name__ == "__main__":
    connect_four()
