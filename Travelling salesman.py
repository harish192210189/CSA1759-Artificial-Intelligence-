from itertools import permutations

cities = ['A', 'B', 'C']
graph = {
    ('A', 'B'): 10, ('A', 'C'): 15,
    ('B', 'A'): 10, ('B', 'C'): 35,
    ('C', 'A'): 15, ('C', 'B'): 30
}

min_cost = float('inf')
best_route = []

for perm in permutations(cities):
    path_cost = 0
    for i in range(len(perm) - 1):
        path_cost += graph.get((perm[i], perm[i + 1]), float('inf'))
    path_cost += graph.get((perm[-1], perm[0]), float('inf'))
    
    if path_cost < min_cost:
        min_cost = path_cost
        best_route = perm

print(f"Minimum cost: {min_cost}, Route: {' -> '.join(best_route)}")
