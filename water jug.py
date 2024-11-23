from collections import deque

capacities = (4, 3)
goal = 2
visited = set()
queue = deque([(0, 0)])
steps = []  

while queue:
    state = queue.popleft()
    if state in visited:
        continue
    visited.add(state)
    steps.append(state)  
    print(f"Step {len(steps)}: {state}")  

    if goal in state:
        print(f"Solution found: {state}")
        break

    a, b = state
    queue.extend([
        (capacities[0], b),  
        (a, capacities[1]),  
        (0, b),              
        (a, 0),              
        (max(0, a - (capacities[1] - b)), min(capacities[1], a + b)),  
        (min(capacities[0], a + b), max(0, b - (capacities[0] - a)))   
    ])
