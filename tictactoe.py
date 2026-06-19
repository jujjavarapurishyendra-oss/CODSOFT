

import math
board = [' ' for _ in range(9)]

def print_board():
    """Prints the current state of the 3x3 board."""
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def is_winner(b, player):
    """Checks if the given player ('X' or 'O') has won the game."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    return any(all(b[cell] == player for cell in combo) for combo in win_conditions)

def is_board_full(b):
    """Returns True if there are no empty spaces left."""
    return ' ' not in b

def minimax(b, depth, is_maximizing):
    """The core Minimax algorithm."""
    if is_winner(b, 'O'):
        return 10 - depth
    if is_winner(b, 'X'):
        return depth - 10
    if is_board_full(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O' 
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

def find_best_move():
    """Iterates through empty cells to find the optimal move for the AI."""
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    """Main game loop managing turns."""
    print("Welcome to Tic-Tac-Toe AI!")
    print("You are 'X' (Plays First) | AI is 'O'")
    print("Enter positions from 1 to 9 corresponding to the board layout.")
    print_board()

    while True:

        try:
            move = int(input("Your turn (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        board[move] = 'X'
        print_board()

        if is_winner(board, 'X'):
            print("Amazing! You won! 🎉")
            break
        if is_board_full(board):
            print("It's a tie! 🤝")
            break

        
        print("AI is calculating its unbeatable move...")
        ai_move = find_best_move()
        if ai_move != -1:
            board[ai_move] = 'O'
        
        print_board()

        if is_winner(board, 'O'):
            print("The AI wins! Unbeatable as promised. 🤖")
            break
        if is_board_full(board):
            print("It's a tie! 🤝")
            break

if __name__ == "__main__":
    play_game()