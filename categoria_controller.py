from flask import Flask, jsonify, request
import json


from categoria_repository import CategoriaRepository



app = Flask(__name__)

@app.route("/ola", methods = ['GET'])
def ola():
    return "minha primeira API"



@app.route("/categorias", methods = ['GET'])
def listar_categorias():
    repo = CategoriaRepository()
    dados = repo.find_all()
    categoria_dic = []
    # # for d in dados: 
    #     categoria_dic.append({'id':d[0],'nome':d[1],'descricao':d[2]})

    cabecalhos = ['id','nome','descricao']
    dados_retorno = [dict(zip(cabecalhos,d)) for d in dados]

    # return jsonify(dados)
    return jsonify(dados_retorno)

@app.route('/categorias/<int:categoriaID>')
def buscar_por_id(categoriaID):
    repo = CategoriaRepository()
    categoria = repo.find_by_id(categoriaID)
    categoria_retorno = {'id':categoria[0], 'nome':categoria[1], 'descricao':categoria[2]}
    return jsonify(categoria_retorno)

@app.route("/categorias", methods = ['POST'])
def cadastrar_categoria():
    repo = CategoriaRepository()

    dados_jason = request.get_json()

    #pegando os dados recebidos JSON
    id = dados_jason.get("id")
    nome = dados_jason.get("nome")
    descricao = dados_jason.get("descricao")

    #enviando para banco de dados
    repo.create(nome,descricao)

    return jsonify({
        "mensagem":"Categoria cadastrada com sucesso.", 
        "nome":nome,
        "descricao":descricao
        
        }),201


@app.route("/categoria/<int:id_categoria>", methods = ['DELETE'])
def remover_categoria(id_categoria):

# objeto de comunicacao com o banco de dados
    repo =CategoriaRepository()

# removendo a categoria do banco de dados
    repo.delete(id_categoria)

    return jsonify({"mensagem":"Categoria removida com sucesso."})


if __name__ == "__main__":
    app.run(debug=True, port=5000)

