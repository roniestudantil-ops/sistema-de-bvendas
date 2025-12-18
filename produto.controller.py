from flask import Flask, jsonify, request, Blueprint
from produto_repository import ProdutoRepository

produto_bp = Blueprint("produto", __name__)
repo = ProdutoRepositoy()

@produto_bp.route("/produtos", methods=["GET"])
def listar_produtos():
    repo = ProdutoRepository()
    dados = repo.find_all()

    cabecalhos = ['id', 'nome', 'descricao', 'preco', 'quantidade_estoque', 'categoria_id']
    dados_retorno = [dict(zip(cabecalhos, d)) for d in dados]

    return jsonify(dados_retorno)

@produto_bp.route("/produtos", methods=["GET"])
def cadastrar_produtos():
    repo = ProdutoRepository()
    dados_json = request.get_json()
     
    if not dados_json.get("nome") or not dados_json.get("preco"):
            return jsonify({"erro": "Campos 'nome' e 'preco' são obrigatórios"}),   

    repo.create(
        dados_json.get("nome"),
        dados_json.get("descricao"),
        dados_json.get("preco"),
        dados_json.get("quantidade_estoque"), # Use minúsculo para facilitar no Postman
        dados_json.get("categoria_id")        # Use minúsculo aqui também
    )
        
    
    
    return jsonify({"Produto cadastrado com sucesso"}),
