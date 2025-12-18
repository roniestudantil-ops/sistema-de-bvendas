from flask import Flask, jsonify
import requests

endereco = Flask(__name__)

@endereco.route("/<cep>")
def get_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    #irá fazer a requisição no servidor
    dados_endereco = requests.get(url)

    endereco_json = dados_endereco.json()
    rua = endereco_json.get("logradouro")
    cidade = endereco_json.get("logradouro")
    estado = endereco_json.get("estado")

    endereco_retorno = {
    "mensagem":"Endereço encontrado com sucesso.",
    "rua":rua,
    "cidade":cidade,
    "estado":estado

    }


    return jsonify(endereco_json)
    #return {"mensagem":"Endereco{cep} econtrado com sucesso."}


if __name__=="__main__":
    endereco.run(debug=True, port=8080)