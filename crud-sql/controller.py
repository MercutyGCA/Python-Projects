import model
from config import conn

conexao = conn.getConnection()

class Crud:
    def __init__(self) -> None:
         self.conexao = conexao
         
    def add(self):
        nome = input('Digite o nome: ')
        idade = input('Digite a idade: ')
        pais = input('Digite o Pais: ')
        model.adicionar(nome, idade, pais)
        model.close()
        
    def update(self):
            id = input('Digite o id de quem será atualizado: ')
            nome = input('Digite o nome: ')
            idade = input('Digite a idade: ')
            pais = input('Digite o Pais: ')
            model.atualizar(id,nome, idade, pais)
            model.close()
        
    def delete(self):
        id = input('Digite o id de quem será deletado: ')
        model.deletar(id)
        model.close()
            
    def searchAll(self):
        model.buscarTodos()
        model.close()
            
    def searchForIF(self):
        id = input('Digite o id a ser buscado: ')
        print(model.buscarPorID(id))
        model.close()

crud = Crud