% Define initial facts
fact(cat).
fact(dog).
fact(mammal(cat)).
fact(mammal(dog)).
fact(tiger).
fact(mammal(tiger)).
fact(rodent(mouse)).
fact(rodent(rat)).

% Define rules
rule(animal(X)) :- mammal(X). % If X is a mammal, then X is an animal.
rule(animal(X)) :- rodent(X).  % If X is a rodent, then X is an animal.

% Query to check if something is an animal
is_animal(X) :- rule(animal(X)).

% Sample queries
% ?- is_animal(cat).
% ?- is_animal(dog).
% ?- is_animal(tiger).
% ?- is_animal(mouse).
