from collections import deque

graph = {
    'A': ['B'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()
queue = deque(['A'])

while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        queue.extend(graph[node])
