% Fruit color facts
fruit_color(apple, red).
fruit_color(banana, yellow).

% Query to find the color of a specific fruit
find_color(Fruit, Color) :- fruit_color(Fruit, Color).

% Query to find all fruits of a specific color
find_fruits_by_color(Color, Fruit) :- fruit_color(Fruit, Color).

% Sample queries:
% ?- find_color(apple, Color).
% ?- find_fruits_by_color(yellow, Fruit).
