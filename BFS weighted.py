from collections import deque, defaultdict

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 1), ('E', 7)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

visited, queue, shortest_paths, parent = set(), deque(['A']), defaultdict(lambda: float('inf')), {}
shortest_paths['A'] = 0

while queue:
    node = queue.popleft()
    if node not in visited:
        visited.add(node)
        for neighbor, weight in graph[node]:
            total_weight = shortest_paths[node] + weight
            if total_weight < shortest_paths[neighbor]:
                shortest_paths[neighbor] = total_weight
                parent[neighbor] = node
                queue.append(neighbor)

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
