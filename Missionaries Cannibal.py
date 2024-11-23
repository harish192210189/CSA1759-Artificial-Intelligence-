from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)
visited = set()
queue = deque([(start, [])])

while queue:
    (m, c, b), path = queue.popleft()
    if (m, c, b) in visited: continue
    visited.add((m, c, b))

    if (m, c, b) == goal:
        for step in path + [(m, c, b)]:
            print(f"State: {step}")
        break

    for m_move, c_move in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
        new_m = m - m_move * b + m_move * (1 - b)
        new_c = c - c_move * b + c_move * (1 - b)
        new_b = 1 - b

        if 0 <= new_m <= 3 and 0 <= new_c <= 3:
            if (new_m == 0 or new_m >= new_c) and (new_m == 3 or (3 - new_m) >= (3 - new_c)):
                queue.append(((new_m, new_c, new_b), path + [(m, c, b)]))
