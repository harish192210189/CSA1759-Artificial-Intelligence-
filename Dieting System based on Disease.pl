% Diet recommendations based on diseases
diet(diabetes, 'Eat low-sugar foods and high-fiber vegetables.').
diet(obesity, 'Focus on portion control and whole grains.').

% Suggest diet based on disease
suggest_diet(Disease, Recommendation) :-
    diet(Disease, Recommendation).

% Sample queries:
% ?- suggest_diet(diabetes, Recommendation).
% ?- suggest_diet(obesity, Recommendation).
