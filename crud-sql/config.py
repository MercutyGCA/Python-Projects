import mysql.connector

class Conexao:
    def __init__(self, user, password, database, host, port):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port

    def getConnection(self):
        conexao = mysql.connector.connect(
            user=self.user,
            password=self.password,
            database=self.database,
            host=self.host,
            port=self.port
        )
        return conexao

conn = Conexao('root', '', 'mercado', '127.0.0.1', '3306')
print(conn.getConnection()._server_status)
#cursor = conexao.cursor()