% Initial state
state(monkey, box, bananas).

% Action to pick up bananas
pick_up(state(monkey, box, bananas), state(monkey, empty, bananas)).

% Action to move box
move(state(monkey, box, bananas), state(monkey, box, bananas)). % No move needed

% Solve the problem
solve(State) :-
    pick_up(State, NewState), write('Picked up: '), write(NewState), nl, !.
solve(State) :-
    move(State, NewState), write('Moved: '), write(NewState), nl, solve(NewState).

% Sample query: ?- state(X), solve(X).
