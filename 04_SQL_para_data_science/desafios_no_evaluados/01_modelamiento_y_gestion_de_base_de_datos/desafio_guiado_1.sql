\c postgres;

DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca;

\c biblioteca;

CREATE TABLE Libro(

    id_libro SERIAL PRIMARY KEY,
    nombre_libro varchar,
    autor varchar,
    genero varchar
);

INSERT INTO LIBRO(nombre_libro, autor, genero) VALUES ('Sapo y Sepo', 'Jorge Guerrero', 'Fantasia');
INSERT INTO LIBRO(nombre_libro, autor, genero) VALUES ('La Metamorfosis', 'Jorge Guerrero', 'Drama');

CREATE TABLE Prestamo(

    id_prestamo SERIAL PRIMARY KEY,
    id_libro integer,
    nombre_persona varchar,
    fecha_inicio date Default current_date,
    fecha_termino date Default current_date + 7,

    FOREIGN KEY (id_libro) REFERENCES LIBRO(id_libro)
);

ALTER TABLE LIBRO ADD COLUMN prestado boolean Default false;

UPDATE LIBRO SET PRESTADO = TRUE WHERE id_libro = 1;
UPDATE LIBRO SET PRESTADO = TRUE WHERE id_libro = 2;

INSERT INTO PRESTAMO(id_libro, nombre_persona) VALUES (1, 'Persona 1');
INSERT INTO PRESTAMO(id_libro, nombre_persona) VALUES (1, 'Persona 2');
INSERT INTO PRESTAMO(id_libro, nombre_persona) VALUES (1, 'Persona 3');
INSERT INTO PRESTAMO(id_libro, nombre_persona) VALUES (1, 'Persona 4');
INSERT INTO PRESTAMO(id_libro, nombre_persona) VALUES (1, 'Persona 5');

INSERT INTO PRESTAMO(id_libro, nombre_persona) VALUES (2, 'Persona 1');
INSERT INTO PRESTAMO(id_libro, nombre_persona) VALUES (2, 'Persona 2');
INSERT INTO PRESTAMO(id_libro, nombre_persona) VALUES (2, 'Persona 3');
INSERT INTO PRESTAMO(id_libro, nombre_persona) VALUES (2, 'Persona 4');
INSERT INTO PRESTAMO(id_libro, nombre_persona) VALUES (2, 'Persona 5');
INSERT INTO PRESTAMO(id_libro, nombre_persona) VALUES (2, 'Persona 6');

INSERT INTO libro(nombre_libro, autor, genero) VALUES ('The Holy Bible', 'Desconocido', 'Religion');

SELECT nombre_libro, nombre_persona FROM LIBRO JOIN PRESTAMO ON LIBRO.id_libro = PRESTAMO.id_libro;

SELECT * FROM PRESTAMO WHERE id_libro = 1 ORDER BY fecha_inicio DESC;

--SELECT * from libro;
--SELECT * from Prestamo;