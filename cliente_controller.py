from flask import Flask, jsonify, request
import json


from cliente_repository import ClienteRepository

app = Flask(__name__)

# @app.route("/clientes", methods = ['GET'])
# def listar_clientes():
#     dados = [{"nome":"Landro"},{"nome":"Maria"},{"nome":"Silvio"},{"nome":"Marta"}]
#     return jsonify(['Leandro','Maria','Silvio','Marta'])

# --- ROTAS DE CLIENTES ---

# --- ROTA DE LISTAR (GET) ---
@app.route("/clientes", methods=["GET"])
def listar_clientes():
    repo = ClienteRepository()
    dados = repo.find_all()
    
    # Transforma a resposta do banco (lista de tuplas) em JSON (lista de dicionários)
    # A ordem da lista 'cabecalhos' deve ser IGUAL à ordem das colunas no seu banco
    cabecalhos = ['id', 'nome', 'cpf', 'email', 'telefone', 'endereco', 'cidade', 'estado', 'cep']
    dados_retorno = [dict(zip(cabecalhos, d)) for d in dados]
    
    return jsonify(dados_retorno)

# --- ROTA DE CADASTRAR (POST) ---
@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    repo = ClienteRepository()
    dados_json = request.get_json()

    # Validação simples: se não tiver nome ou CPF, avisa erro
    if not dados_json.get("nome") or not dados_json.get("cpf"):
        return jsonify({"erro": "Campos 'nome' e 'cpf' são obrigatórios"}), 400

    repo.create(
        dados_json.get("nome"),
        dados_json.get("cpf"),
        dados_json.get("email"),
        dados_json.get("telefone"),
        dados_json.get("endereco"),
        dados_json.get("cidade"),
        dados_json.get("estado"),
        dados_json.get("cep")
    )

    return jsonify({"mensagem": "Cliente cadastrado com sucesso!"}), 201