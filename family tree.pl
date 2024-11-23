% Family relationships
parent(john, mary). parent(john, david).
parent(susan, mary). parent(susan, david).
parent(mary, alice). parent(mary, charlie).
parent(david, eve).

% Define relationships
mother(M, C) :- parent(M, C), female(M).
father(F, C) :- parent(F, C), male(F).
sibling(S1, S2) :- parent(P, S1), parent(P, S2), S1 \= S2.
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).

% Gender definitions
female(susan). female(mary). female(alice). female(charlie). female(eve).
male(john). male(david).

% Sample queries:
% ?- parent(X, mary).
% ?- sibling(david, Sibling).
% ?- grandparent(GP, alice).
