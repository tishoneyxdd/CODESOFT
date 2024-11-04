import math
from board import check_winner, is_board_full

def minimax(board, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':  # AI wins
        return 1
    elif winner == 'O':  # Human wins
        return -1
    elif is_board_full(board):  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    score = minimax(board, False, alpha, beta)
                    board[i][j] = ''
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    score = minimax(board, True, alpha, beta)
                    board[i][j] = ''
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'X'
                score = minimax(board, False, -math.inf, math.inf)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = 'X'
    return move
