from collections import defaultdict

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 1), ('E', 7)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

def dfs(node, current_weight):
    visited.add(node)
    for neighbor, edge_weight in graph[node]:
        total_weight = current_weight + edge_weight
        if total_weight < shortest_paths[neighbor]:
            shortest_paths[neighbor] = total_weight
            parent[neighbor] = node
            if neighbor not in visited:
                dfs(neighbor, total_weight)

visited, shortest_paths, parent = set(), defaultdict(lambda: float('inf')), {}
shortest_paths['A'] = 0
parent['A'] = None

dfs('A', 0)

if shortest_paths['F'] != float('inf'):
    path, end = [], 'F'
    while end in parent:
        path.append(end)
        end = parent[end]
    path.append('A')
    print(f"Shortest path from A to F: {shortest_paths['F']}, Path: ", end='')
    for node in path[::-1]:
        print(node, end=' -> ' if node != 'A' else '')
    print()
else:
    print("Shortest path from A to F: unreachable")
