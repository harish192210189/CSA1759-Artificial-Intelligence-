% Define symptoms and their associated diseases
symptom(cough, flu).
symptom(fever, flu).

symptom(cough, cold).
symptom(runny_nose, cold).

% Rule to diagnose disease based on symptoms
diagnose(Disease, Symptoms) :-
    findall(Disease, (member(Symptom, Symptoms), symptom(Symptom, Disease)), Diseases),
    list_to_set(Diseases, UniqueDiseases),  % Remove duplicates
    UniqueDiseases \= [].

% Sample query to diagnose based on symptoms
% ?- diagnose(Disease, [cough, fever]).
