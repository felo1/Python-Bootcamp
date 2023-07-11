CREATE DATABASE Futbol;

USE futbol;

CREATE TABLE Equipos (
	equipo_id INT PRIMARY KEY,
    nombre VARCHAR(59)
);

CREATE TABLE Jugadores (
	jugador_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    edad INT,
    equipo_id INT,
    FOREIGN KEY(equipo_id) REFERENCES Equipos(equipo_id)
);

CREATE TABLE Partidos (
	partido_id INT PRIMARY KEY AUTO_INCREMENT,
    equipo_id INT,
    resultado VARCHAR(10),
    temporada VARCHAR(10),
    FOREIGN KEY(equipo_id) REFERENCES Equipos(equipo_id)
);


CREATE TABLE Estadisticas (
	estadistica_id INT PRIMARY KEY AUTO_INCREMENT,
    jugador_id INT,
    goles INT,
    temporada VARCHAR(10),
    FOREIGN KEY(jugador_id) REFERENCES Jugadores(jugador_id)
);

INSERT INTO Equipos
VALUES
(1, 'ñublense'),
(2, 'wanderers'),
(3, 'niubi');

INSERT INTO Jugadores (nombre, edad, equipo_id)
VALUES
('Eduardo', 23, 3),
('Geronimo', 24, 1),
('Tomas', 30, 2),
('Juan', 28, 3),
('Leandro', 19, 1);

INSERT INTO Partidos (equipo_id, resultado, temporada)
VALUES 
(1, 'Victoria', 2022),
(2, 'Empate', 2022),
(3, 'Empate', 2022),
(1, 'Victoria', 2023),
(2, 'Derrota', 2023),
(3, 'Victoria', 2023);

INSERT INTO Estadisticas (jugador_id, goles, temporada)
VALUES
(1, 3, 2022),
(2, 0, 2022),
(3, 2, 2022),
(4, 0, 2022),
(5, 4, 2022),
(1, 2, 2023),
(2, 0, 2023),
(3, 0, 2023),
(4, 1, 2023),
(5, 5, 2023);

SELECT * FROM Estadisticas;

SELECT * FROM Jugadores WHERE equipo_id = 3;

SELECT jugador_id, SUM(goles) AS total_goles
FROM Estadisticas
WHERE temporada = '2023'
GROUP BY jugador_id;

SELECT DISTINCT equipo_id
FROM Partidos
WHERE resultado = 'Victoria'
AND (SELECT count(*) FROM Partidos p2 WHERE p2.equipo_id = Partidos.equipo_id) >= 1;

SELECT jugador_id
FROM Jugadores
WHERE jugador_id NOT IN (SELECT jugador_id FROM Partidos WHERE temporada = '2022');

SELECT avg(edad) AS promedio_edad
FROM Jugadores
WHERE equipo_id = 3;