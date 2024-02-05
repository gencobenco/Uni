import pygame

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_SIZE = (800, 570)
CELL_SIZE = 80
ROWS = 6
COLS = 7
HEIGHT = ROWS * CELL_SIZE + CELL_SIZE
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Connect Four")

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Create the game board
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

# Function to draw the game board
def draw_board():
    screen.fill(BLACK)

    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE + CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.circle(screen, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 'X':
                pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, YELLOW, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)

# Function to check if a player has won
def check_win(player):
    # Check rows
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True

    # Check columns
    for col in range(COLS):
        for row in range(ROWS - 3):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True

    # Check diagonals (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True

    # Check diagonals (top-right to bottom-left)
    for row in range(ROWS - 3):
        for col in range(3, COLS):
            if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == player and board[row+3][col-3] == player:
                return True

    return False

# Game loop
running = True
turn = 'X'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the column where the player clicked
            col = event.pos[0] // CELL_SIZE

            # Find the first empty row in the selected column
            for row in range(ROWS - 1, -1, -1):
                if board[row][col] == ' ':
                    board[row][col] = turn
                    break

            # Switch turns
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

    # Draw the game board
    draw_board()

    # Check for a win
    if check_win('X'):
        print("ROTER Spieler gewinnt!")
        running = False
    elif check_win('O'):
        print("GELBER Spieler gewinnt!")
        running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()