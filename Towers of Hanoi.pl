% Move N disks from Source to Target using Auxiliary as a helper.
move(N, Source, Target, Auxiliary) :-
    N > 0,
    N1 is N - 1,
    move(N1, Source, Auxiliary, Target),
    write('Move disk from '), write(Source), write(' to '), write(Target), nl,
    move(N1, Auxiliary, Target, Source).

% move(3, a, c, b).
