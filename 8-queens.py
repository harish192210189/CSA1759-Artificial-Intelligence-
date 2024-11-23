n = 8
board = [-1] * n
solution = None

def safe(r, c):
    return all(board[i] != c and abs(board[i] - c) != r - i for i in range(r))

def solve(r=0):
    global solution
    if solution: 
        return
    if r == n:
        solution = board[:]
    else:
        for c in range(n):
            if safe(r, c):
                board[r] = c
                solve(r + 1)

solve()

if solution:
    for row in range(n):
        print(' '.join('Q' if col == solution[row] else '.' for col in range(n)))
