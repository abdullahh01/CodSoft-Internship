import random

# The Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print('-' * 9)

# Function to check if the board is full
def is_board_full(board):
    return all(cell != ' ' for cell in board)

# Function to check if a player has won
def check_win(board, player):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if check_win(board, 'X'):
        return 1
    if check_win(board, 'O'):
        return -1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Function to find the best move for AI
def find_best_move(board):
    best_move = -1
    best_eval = float('-inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            eval = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    while True:
        if not is_board_full(board) and not check_win(board, 'X') and not check_win(board, 'O'):
            move = -1
            while move < 0 or move >= 9 or board[move] != ' ':
                move = int(input("Enter your move (0-8): "))
            board[move] = 'O'
            print_board()

        if check_win(board, 'O'):
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        ai_move = find_best_move(board)
        board[ai_move] = 'X'
        print("AI's move:")
        print_board()

        if check_win(board, 'X'):
            print("AI wins!")
            break

# Start the game
play_game()