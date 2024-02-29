import pygame
import sys
import math
import numpy as np
import random

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Farben der Spieler
PLAYER1_COLOR = RED
PLAYER2_COLOR = YELLOW

# Größe des Spielfelds
ROW_COUNT = 6
COLUMN_COUNT = 7


# Größe der Felder
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)

# Erstellt das Spielfeld
def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT))

# Checkt ob die Spalte noch frei ist
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

# Checkt die nächste freie Reihe
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# Setzt den Stein
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Gibt das Spielfeld aus
def print_board(board):
    print(np.flip(board, 0))

# Checkt ob jemand gewonnen hat
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

    return False

# Zeichnet das Spielfeld
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, PLAYER1_COLOR, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, PLAYER2_COLOR, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

# Zeichnet die Startseite
def draw_start_page():
    screen.fill(BLACK)

    # Draw the welcome message
    welcome_label = myfont.render("4-Gewinnt", 1, WHITE)
    welcome_rect = welcome_label.get_rect(center=(width // 2, SQUARESIZE))
    screen.blit(welcome_label, welcome_rect.topleft)

    # Draw the button rectangle with rounded corners
    button_rect = pygame.Rect(width // 4, height // 3, width // 2, SQUARESIZE)
    pygame.draw.rect(screen, RED, button_rect, border_radius=20)

    # Draw lines to create the border
    pygame.draw.line(screen, BLACK, button_rect.topleft, button_rect.topright, 5)
    pygame.draw.line(screen, BLACK, button_rect.topleft, button_rect.bottomleft, 5)
    pygame.draw.line(screen, BLACK, button_rect.topright, button_rect.bottomright, 5)
    pygame.draw.line(screen, BLACK, button_rect.bottomleft, button_rect.bottomright, 5)

    start_label = myfont.render("Start", 1, WHITE)
    label_rect = start_label.get_rect(center=button_rect.center)
    screen.blit(start_label, label_rect.topleft)

    #Zähler
    PLAYER2_COLOR_count_label = myfont.render(f"Player 2: {Counter_PLAYER2}", 1, PLAYER2_COLOR)
    PLAYER1_COLOR_count_label = myfont.render(f"Player 1: {Counter_PLAYER1}", 1, PLAYER1_COLOR)

    # Clear the old scores
    pygame.draw.rect(screen, BLACK, (10, height - SQUARESIZE, 200, PLAYER2_COLOR_count_label.get_height()))
    pygame.draw.rect(screen, BLACK, (10, height - 2 * SQUARESIZE, 200, PLAYER1_COLOR_count_label.get_height()))

    # sagt nur Score
    score_label = myfont.render(f"Score:", 1, WHITE)
    screen.blit(score_label, (10, 10))

    # Draw the new scores
    screen.blit(PLAYER2_COLOR_count_label, (10, 70))
    screen.blit(PLAYER1_COLOR_count_label, (10, 40))

    # Draw the start button
    start_button_rect = pygame.Rect(width // 4, height // 3, width // 2, SQUARESIZE)
    pygame.draw.rect(screen, RED, start_button_rect, border_radius=20)
    start_label = myfont.render("Start", 1, WHITE)
    label_rect = start_label.get_rect(center=start_button_rect.center)
    screen.blit(start_label, label_rect.topleft)

    # Draw the options button
    options_button_rect = pygame.Rect(width // 4, 2 * height // 3, width // 2, SQUARESIZE)
    pygame.draw.rect(screen, GREY, options_button_rect, border_radius=20)
    options_label = myfont.render("Options", 1, WHITE)
    label_rect = options_label.get_rect(center=options_button_rect.center)
    screen.blit(options_label, label_rect.topleft)

    pygame.display.update()

    return start_button_rect, options_button_rect

# Zeichnet die Optionsseite
def draw_options_page():
    screen.fill(BLACK)

    # Draw the options message
    options_label = myfont.render("Options", 1, WHITE)
    options_rect = options_label.get_rect(center=(width // 2, SQUARESIZE))
    screen.blit(options_label, options_rect.topleft)

    # Draw a back button
    back_button_rect = pygame.Rect(width // 4, 2 * height // 3, width // 2, SQUARESIZE)
    pygame.draw.rect(screen, RED, back_button_rect, border_radius=20)
    back_label = myfont.render("Back", 1, WHITE)
    label_rect = back_label.get_rect(center=back_button_rect.center)
    screen.blit(back_label, label_rect.topleft)

    # Draw color options for the first piece
    color1_button_rect = pygame.Rect(width // 4, height // 3, width // 2, SQUARESIZE)
    pygame.draw.rect(screen, PLAYER1_COLOR, color1_button_rect, border_radius=20)
    color1_label = myfont.render("Color 1", 1, BLACK)
    label_rect = color1_label.get_rect(center=color1_button_rect.center)
    screen.blit(color1_label, label_rect.topleft)

    # Draw color options for the second piece
    color2_button_rect = pygame.Rect(width // 4, height // 2, width // 2, SQUARESIZE)
    pygame.draw.rect(screen, PLAYER2_COLOR, color2_button_rect, border_radius=20)
    color2_label = myfont.render("Color 2", 1, BLACK)
    label_rect = color2_label.get_rect(center=color2_button_rect.center)
    screen.blit(color2_label, label_rect.topleft)

    pygame.display.update()

    
    return back_button_rect, color1_button_rect, color2_button_rect

# Wechselt den Spieler
def next_turn(turn):
    return (turn + 1) % 2

# Animation für das Fallen der Steine
def animate_piece_drop(board, row, col, piece):
    drop_speed = 0
    while drop_speed < (ROW_COUNT - row) * SQUARESIZE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
        pygame.draw.rect(screen, BLACK, (col * SQUARESIZE, 0, SQUARESIZE, SQUARESIZE))
        if piece == 1:
            pygame.draw.circle(screen, PLAYER1_COLOR, (int(col * SQUARESIZE + SQUARESIZE / 2), int(drop_speed + SQUARESIZE / 2)), RADIUS)
        else:
            pygame.draw.circle(screen, PLAYER2_COLOR, (int(col * SQUARESIZE + SQUARESIZE / 2), int(drop_speed + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()
        pygame.time.wait(15)  # Decrease delay between each frame
        drop_speed += 20  # Increase amount of pixels the piece moves each frame
        draw_board(board)
    drop_piece(board, row, col, piece)  # Update the board state after the animation

# Checkt obs unentschieden ist
def is_draw(board):
    return not 0 in board

# Timer
def time_counter():
    myfont = pygame.font.SysFont("freesansbold.ttf", 25)
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    timer_label = myfont.render("{:02d}:{:02d}".format(minutes, seconds), 1, WHITE)
    pygame.draw.rect(screen, BLACK, (655, 0, 100, timer_label.get_height()))  # Clear the old timer label
    screen.blit(timer_label, (655, 0)) 
    pygame.display.update()
    
# Main game loop vorbereitung
pygame.init()
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("freesansbold.ttf", 30)
start_ticks = pygame.time.get_ticks()  # starter tick
last_update_time = 0

# Variable für Startseite
on_start_page = True
on_options_page = False

buffer_surface = pygame.Surface((width, height))

Counter_PLAYER2 = 0
Counter_PLAYER1 = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False                     #
            pygame.quit()             # eventuell bug gefixt wo man es nicht schließen konnte
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if on_start_page:
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    on_start_page = False
                elif options_button_rect.collidepoint(mouse_x, mouse_y):
                    on_start_page = False
                    on_options_page = True
            elif on_options_page:
                if back_button_rect.collidepoint(mouse_x, mouse_y):
                    on_options_page = False
                    on_start_page = True
                elif color1_button_rect.collidepoint(mouse_x, mouse_y):
                    PLAYER1_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                elif color2_button_rect.collidepoint(mouse_x, mouse_y):
                    PLAYER2_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  

    buffer_surface.fill(BLACK)

    if on_start_page:
        start_button_rect, options_button_rect = draw_start_page()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    on_start_page = False
                elif options_button_rect.collidepoint(mouse_x, mouse_y):
                    on_start_page = False
                    on_options_page = True
    elif on_options_page:
        back_button_rect, color1_button_rect, color2_button_rect = draw_options_page()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if back_button_rect.collidepoint(mouse_x, mouse_y):
                    on_options_page = False
                    on_start_page = True
                elif color1_button_rect.collidepoint(mouse_x, mouse_y):
                    PLAYER1_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                elif color2_button_rect.collidepoint(mouse_x, mouse_y):
                    PLAYER2_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    else:
        # Spiel starten
        board = create_board()
        print_board(board)
        draw_board(board)  # Zeichnet das Spielfeld
        game_over = False
        turn = 0
        start_ticks = pygame.time.get_ticks()  # Resettet Timer am Anfang jeder Runde
        screen.blit(buffer_surface, (0, 0))
        pygame.display.update()

        while not game_over:
            draw_board(board)
            time_counter()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    posx = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(screen, PLAYER1_COLOR, (posx, int(SQUARESIZE / 2)), RADIUS)
                        turn_label = myfont.render("Player 1's turn", 1, PLAYER1_COLOR)
                    else:
                        pygame.draw.circle(screen, PLAYER2_COLOR, (posx, int(SQUARESIZE / 2)), RADIUS)
                        turn_label = myfont.render("Player 2's turn", 1, PLAYER2_COLOR)
                    screen.blit(turn_label, (0, 0))
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))
                    
                    if is_draw(board):
                        label = myfont.render("Unentschieden", 1, WHITE)
                        screen.blit(label, (0, 0))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        game_over = True

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        animate_piece_drop(board, row, col, turn + 1)  # Animation im Loop

                        if winning_move(board, turn + 1):
                            label = myfont.render(f"Player {turn + 1} wins!!", 1, PLAYER1_COLOR if turn == 0 else PLAYER2_COLOR)
                            screen.blit(label, (0, 0))
                            if turn == 0:
                                Counter_PLAYER1 += 1
                            else:
                                Counter_PLAYER2 += 1

                            game_over = True

                        
                        print_board(board)
                        draw_board(board)

                        turn = next_turn(turn)
                        
                        if game_over:
                            pygame.time.wait(3000)

        on_start_page = True  # Zurück zur Startseite nach dem Spiel

    pygame.display.update()