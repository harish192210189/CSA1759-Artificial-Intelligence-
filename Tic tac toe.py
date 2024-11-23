board = [' ']*9
player = 'X'

for turn in range(9):
    print('\n'.join(['|'.join(board[i:i+3]) for i in range(0, 9, 3)]))
    move = int(input(f"Player {player}, enter your move (from 1 to 9): ")) - 1
    if board[move] == ' ': 
        board[move] = player
        if any(all(board[i] == player for i in combo) for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]):
            print(f"Player {player} wins!")
            break
        player = 'O' if player == 'X' else 'X'
else:
    print("It's a draw!")
