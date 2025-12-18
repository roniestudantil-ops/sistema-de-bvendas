from conexao import Conexao

class ProdutoRepository:
    def __init__(self):
        self.conexao = Conexao()

    def create(self, nome, descricao, preco, quantidade_estoque, categoria_id):
        cursor = self.conexao.get_cursor()
        
        sql = """
            INSERT INTO Produto (Nome, Descricao, Preco, QuantidadeEstoque, CategoriaID)
            VALUES (%s, %s, %s, %s, %s)
        """
        
        cursor.execute(sql, (nome, descricao, preco, quantidade_estoque, categoria_id))
        
        # O commit que corrigimos anteriormente:
        self.conexao.get_conexao().commit()

    def find_all(self):
        cursor = self.conexao.get_cursor()
        sql = "SELECT * FROM Produto"
        cursor.execute(sql)
        produtos = cursor.fetchall()
        return produtos