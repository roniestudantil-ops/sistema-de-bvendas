
from conexao import Conexao

class ClienteRepository:
    def __init__(self):
        # Aqui usamos a classe Conexao igualzinho ao categoria_repository
        self.conexao = Conexao()

    def create(self, nome, cpf, email, telefone, endereco, cidade, estado, cep):
        # Pede o cursor para a sua classe de conexão
        cursor = self.conexao.get_cursor()
        
        sql = """
            INSERT INTO Cliente (Nome, CPF, Email, Telefone, Endereco, Cidade, Estado, CEP)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (nome, cpf, email, telefone, endereco, cidade, estado, cep))
        
       
        self.conexao.get_conexao().commit()
        # cursor.close() # (Opcional, dependendo de como sua classe Conexao foi feita)

    def find_all(self):
        cursor = self.conexao.get_cursor()
        sql = "SELECT * FROM Cliente"
        cursor.execute(sql)
        clientes = cursor.fetchall()
        return clientes