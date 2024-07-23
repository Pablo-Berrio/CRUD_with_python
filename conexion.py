import mysql.connector

class Conexion:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    #_instance = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database = self.database
            )
            print("Conexion Exitosa a la base de datos")
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos")


    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión Cerrada")

    def execute_query(self, query, params = None):
        cursor = self.connection.cursor(buffered = True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Consulta Ejecutada de manera exitosa")
            if query.lower().startswith('select'):
                result = cursor.fetchall()
                return result
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta", err)
            return None
        finally:
            cursor.close()


