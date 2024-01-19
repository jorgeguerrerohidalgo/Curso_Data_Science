# Manejo bases de datos
import psycopg2

#Objeto de coneccion
conn = psycopg2.connect("user='postgres' password='postgres' host='localhost' port='5433' dbname='beffermann_daniel'")

def postgres(conn, instruccion):
    #Cursor.
    cursor = conn.cursor()

    #Indicar el proceso a ejecutar en postgreSQL.
    cursor.execute(instruccion)

    try:
        #Recuperar resultados.
        return cursor.fetchall()
    except:
        #Guardar los cambios.
        conn.commit()
        print('Se guardaron los cambios en la tabla')
        

    #Cerrar coneccion.
    cursor.close()
    conn.close()