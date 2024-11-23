% Define the graph as edges
% Define the graph as edges with costs
edge(a, b, 1).
edge(a, c, 4).
edge(b, d, 2).
edge(b, g, 3).
edge(c, g, 5).
edge(d, g, 1).

% Heuristic values for each node
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 3).
heuristic(d, 1).
heuristic(g, 0).

% Best First Search algorithm
best_first_search(Start, Goal, Path, Cost) :-
    bfs([[Start]], Goal, Path, Cost).

bfs([[Goal | Visited] | _], Goal, [Goal | Visited], 0). % Goal reached
bfs([[Node | Visited] | Rest], Goal, Path, Cost) :-
    findall([Next, [Next, Node | Visited], StepCost],
            (edge(Node, Next, StepCost),
             \+ member(Next, [Node | Visited]),
             heuristic(Next, Heuristic),
             TotalCost is StepCost + Heuristic),
            Children),
    sort(Children, SortedChildren), % Sort by total cost (step + heuristic)
    append(SortedChildren, Rest, NewQueue),
    bfs(NewQueue, Goal, Path, Cost).

% Sample query
% ?- best_first_search(a, g, Path, Cost).


