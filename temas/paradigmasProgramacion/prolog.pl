%Vamos a usar un ejemplo en el que definimos algunos hechos Y para determinar las relaciones de parentesco.

% Hechos: estas son relaciones que ya sabemos que son verdaderas.
padre(juan, maria).   % Juan es padre de María.
padre(juan, pedro).   % Juan es padre de Pedro.
madre(ana, maria).    % Ana es madre de María.
madre(ana, pedro).    % Ana es madre de Pedro.

% Regla: un padre es progenitor de alguien si tiene un hijo.
progenitor(X, Y) :- padre(X, Y).    % Si X es padre de Y, X es progenitor de Y.
progenitor(X, Y) :- madre(X, Y).    % Si X es madre de Y, X es progenitor de Y.

% Regla: dos personas son hermanos si tienen al mismo padre y madre.
hermanos(X, Y) :- padre(P, X), padre(P, Y), madre(M, X), madre(M, Y), X \= Y.


%puedes ejecutar el codigo -> "?- progenitor(juan, X)." -> pregunta si juan es progenitos de alguien(x)
