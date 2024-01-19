\c postgres;

DROP DATABASE if exists  spotify_2018;
CREATE DATABASE spotify_2018;

\c spotify_2018;

CREATE TABLE artista(
    nombre_artista varchar, 
    fecha_de_nacimiento date, 
    nacionalidad varchar, 
    PRIMARY KEY (nombre_artista));

CREATE TABLE album(
    titulo_album varchar, 
    artista varchar, 
    anio integer, 
    PRIMARY KEY (titulo_album), 
    FOREIGN KEY (artista) REFERENCES artista(nombre_artista));

CREATE TABLE cancion(
    titulo_cancion varchar, 
    artista varchar, 
    album varchar, 
    numero_del_track integer, 
    PRIMARY KEY (titulo_cancion), 
    FOREIGN KEY (album) REFERENCES album(titulo_album));



--Insertando valores en una tabla
\copy artista(nombre_artista, fecha_de_nacimiento, nacionalidad) from 'Artista.csv' delimiter ',' csv header;
\copy album(titulo_album, artista, anio) from 'Album.csv' delimiter ',' csv header;
\copy cancion(titulo_cancion, artista, album, numero_del_track) from 'Cancion.csv' delimiter ',' csv header;


-- Canciones Lanzadas el año 2018

SELECT CANCION.titulo_cancion, Album.anio FROM Album JOIN CANCION ON ALBUM.titulo_album=CANCION.album WHERE ALBUM.anio = 2018;

-- Album y nacionalidad del artista

SELECT ALBUM.titulo_album, ARTISTA.nacionalidad FROM ARTISTA JOIN ALBUM ON ALBUM.artista=ARTISTA.nombre_artista;

-- Número de track, canción, album, año de lanzamiento y artista donde las canciones, 
-- deberán estar ordenadas por año de lanzamiento del álbum, álbum y artista correspondiente.

SELECT CANCION.numero_del_track, CANCION.titulo_cancion, CANCION.album, Album.anio, CANCION.artista 
FROM Album JOIN CANCION ON ALBUM.titulo_album=CANCION.album
ORDER BY Album.anio, CANCION.album, CANCION.artista;
