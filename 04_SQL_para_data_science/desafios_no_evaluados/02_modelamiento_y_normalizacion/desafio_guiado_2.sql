select
*
from cancion
where numero_del_track = 4
and artista in (
				select
				nombre_artista
				from artista
				where nacionalidad like '%unidense%'
				and date_part('year', fecha_de_nacimiento) > 1992
				limit 1
             )
;