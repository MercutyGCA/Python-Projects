import config

cursor = config.cursor
conexao = config.conexao

class Model:
    def __init__(self):
        self.cursor = cursor
        self.conexao = conexao
        
    def adicionar(self, nome, idade, pais):
        sql = f'INSERT INTO pessoa (nome, idade, pais) VALUES ("{nome}", "{idade}", "{pais}")'
        self.cursor.execute(sql)
        return self.conexao.commit()
    
    def atualizar(self, id, nome, idade, pais):
        sql = f'UPDATE pessoa SET nome = "{nome}",  idade = "{idade}", pais = "{pais}" WHERE idpessoa = "{id}"'
        self.cursor.execute(sql)
        return self.conexao.commit()
    
    def deletar(self, id):
        sql = f'DELETE FROM pessoa WHERE idpessoa = "{id}"'
        self.cursor.execute(sql)
        return self.conexao.commit()
    
    def buscarTodos(self):
        sql = 'SELECT * FROM pessoa'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        
        
    def buscarPorID(self, id):
        sql = f'SELECT * FROM pessoa WHERE idpessoa = "{id}"'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
modelo = Model()

close = conexao.close
adicionar = modelo.adicionar
atualizar = modelo.atualizar
deletar = modelo.deletar
buscarTodos = modelo.buscarTodos
buscarPorID = modelo.buscarPorID