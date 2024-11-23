board = [' ']*9
player = 'X'

def print_board():
    print('\n'.join(['|'.join(board[i:i+3]) for i in range(0, 9, 3)]))

def check_winner(b):
    for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] != ' ':
            return b[combo[0]]
    return None

def alpha_beta(b, depth, alpha, beta, is_max):
    score = {'X': 10, 'O': -10, None: 0}
    winner = check_winner(b)
    if winner: return score[winner]
    if all(x != ' ' for x in b): return 0
    if is_max:
        best = -float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = player
                best = max(best, alpha_beta(b, depth + 1, alpha, beta, False))
                b[i] = ' '
                alpha = max(alpha, best)
                if beta <= alpha: break
        return best
    else:
        best = float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O' if player == 'X' else 'X'
                best = min(best, alpha_beta(b, depth + 1, alpha, beta, True))
                b[i] = ' '
                beta = min(beta, best)
                if beta <= alpha: break
        return best

for turn in range(9):
    print_board()
    if player == 'X':
        move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
        if board[move] != ' ': continue
    else:
        best_val = -float('inf')
        alpha, beta = -float('inf'), float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                move_val = alpha_beta(board, 0, alpha, beta, False)
                board[i] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = i
        board[best_move] = 'O'

    if check_winner(board) is not None:
        print_board()
        print(f"Player {player} wins!")
        break
    player = 'O' if player == 'X' else 'X'
else:
    print_board()
    print("It's a draw!")
