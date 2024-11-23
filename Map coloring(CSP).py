colors = ['Red', 'Green', 'Blue']
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

assignments = {}
nodes = list(graph.keys())

def is_valid(node, color):
    return all(assignments.get(neighbor) != color for neighbor in graph[node])

def backtrack(index):
    if index == len(nodes):
        print(assignments)
        return True
    node = nodes[index]
    for color in colors:
        if is_valid(node, color):
            assignments[node] = color
            if backtrack(index + 1):
                return True
            del assignments[node]
    return False

backtrack(0)
