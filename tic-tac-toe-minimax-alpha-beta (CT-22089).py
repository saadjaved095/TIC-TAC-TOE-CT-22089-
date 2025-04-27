import time
import random

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print('-------------')
    for row in board:
        print('|', end=' ')
        for cell in row:
            print(cell, end=' | ')
        print('\n-------------')

def is_moves_left(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return True
    return False

def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'O':
                return 10
            elif board[row][0] == 'X':
                return -10
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'O':
                return 10
            elif board[0][col] == 'X':
                return -10
    
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'O':
            return 10
        elif board[0][0] == 'X':
            return -10
    
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'O':
            return 10
        elif board[0][2] == 'X':
            return -10
    
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best
    
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best

def minimax_alpha_beta(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax_alpha_beta(board, depth + 1, not is_max, alpha, beta))
                    board[i][j] = ' '
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax_alpha_beta(board, depth + 1, not is_max, alpha, beta))
                    board[i][j] = ' '
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    start_time = time.time()
    best_val = -1000
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return best_move, execution_time

def find_best_move_alpha_beta(board):
    start_time = time.time()
    best_val = -1000
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax_alpha_beta(board, 0, False, -1000, 1000)
                board[i][j] = ' '
                
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return best_move, execution_time

def play_game():
    board = create_board()
    print("Tic-Tac-Toe Game: You (X) vs AI (O)")
    print("Enter row (0-2) and column (0-2) separated by space")
    
    minimax_time_total = 0
    alpha_beta_time_total = 0
    moves_count = 0
    
    while is_moves_left(board) and evaluate(board) == 0:
        print_board(board)
        
        try:
            row, col = map(int, input("Your move (row col): ").split())
            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
                print("Invalid move! Try again.")
                continue
        except:
            print("Invalid input! Enter row and column as numbers separated by space.")
            continue
        
        board[row][col] = 'X'
        
        if evaluate(board) == -10:
            print_board(board)
            print("You win!")
            break
        
        if not is_moves_left(board):
            print_board(board)
            print("It's a tie!")
            break
        
        minimax_move, minimax_time = find_best_move(board)
        minimax_time_total += minimax_time
        
        alpha_beta_move, alpha_beta_time = find_best_move_alpha_beta(board)
        alpha_beta_time_total += alpha_beta_time
        moves_count += 1
        
        board[alpha_beta_move[0]][alpha_beta_move[1]] = 'O'
        print(f"AI moved at position: {alpha_beta_move[0]} {alpha_beta_move[1]}")
        
        if evaluate(board) == 10:
            print_board(board)
            print("AI wins!")
            break
        
        if not is_moves_left(board):
            print_board(board)
            print("It's a tie!")
            break
    
    if moves_count > 0:
        print("\nPerformance Comparison:")
        print(f"Standard Minimax total time: {minimax_time_total:.6f} seconds")
        print(f"Alpha-Beta Pruning total time: {alpha_beta_time_total:.6f} seconds")
        print(f"Improvement: {(1 - alpha_beta_time_total/minimax_time_total) * 100:.2f}%")

if __name__ == "__main__":
    play_game()
