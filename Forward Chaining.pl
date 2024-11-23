% Define initial facts
fact(cat).
fact(mammal).
fact(tiger).

% Define rules
rule(mammal(X)) :- fact(cat).
rule(mammal(X)) :- fact(tiger).

rule(rodent(X)) :- fact(mouse).

rule(animal(X)) :- rule(mammal(X)).
rule(animal(X)) :- rule(rodent(X)).

% Query to infer if something is an animal based on existing facts
infer_animal(X) :- rule(animal(X)).

% Sample queries
% ?- infer_animal(X).
% ?- fact(mammal).
