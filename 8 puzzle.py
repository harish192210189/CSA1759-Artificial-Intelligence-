import heapq

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

start = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
pq, visited = [(0, 0, start, [])], set()

while pq:
    f, g, state, path = heapq.heappop(pq)
    t_state = tuple(map(tuple, state))
    if t_state in visited: continue
    visited.add(t_state)
    if state == goal:
        for step in path + [state]: print('\n'.join(' '.join(str(x) if x else ' ' for x in row) for row in step), '\n')
        break
    i, j = next((x, y) for x in range(3) for y in range(3) if state[x][y] == 0)
    for di, dj in moves:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            heapq.heappush(pq, (g + 1 + sum(abs((val - 1) // 3 - x) + abs((val - 1) % 3 - y) 
                             for x, row in enumerate(new_state) for y, val in enumerate(row) if val), g + 1, new_state, path + [state]))
