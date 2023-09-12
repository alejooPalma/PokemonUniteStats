import mysql.connector as cn
import mysql.connector.errors as ex

class conexion():
    def aegislash():
        try:
            cx = cn.connect(
                user = "root",
                password = "",
                host = "localhost",
                port = "3306", #Para el wampserver
                database="pokemon_unite"
            )

            cur = cx.cursor()#Para recibir respuesta
            consulta= "SELECT * FROM aegislash"
            cur.execute(consulta) #Se establece la conexion.

            datos = list(cur)

            cur.close() #Para finalizar el metodo y que no consuma ram
            cx.close() #Cerrar la conexion con la db
            return datos

        except ex as err:
            print("Error de conexion: "+str(err))

    def azumaril():
        try:
            cx = cn.connect(
                user = "root",
                password = "",
                host = "localhost",
                port = "3306", #Para el wampserver
                database="pokemon_unite"
            )

            cur = cx.cursor()#Para recibir respuesta
            consulta= "SELECT * FROM azumaril"
            cur.execute(consulta) #Se establece la conexion.

            datos = list(cur)

            cur.close() #Para finalizar el metodo y que no consuma ram
            cx.close() #Cerrar la conexion con la db
            return datos

        except ex as err:
            print("Error de conexion: "+str(err))

