states = [(0, 'dirty'), (1, 'dirty')]  
goal = [(0, 'clean'), (1, 'clean')] 
path = []

while states != goal:
    for i, (room, status) in enumerate(states):
        if status == 'dirty':
            path.append(f"Clean room {room}")
            states[i] = (room, 'clean')
        path.append(f"Move to room {1 - room}")

for action in path:
    print(action)
