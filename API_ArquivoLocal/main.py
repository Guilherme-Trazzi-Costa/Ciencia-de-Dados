#Arquivo principal da API

#pip install flask
from flask import Flask, request, make_response, jsonify

#Importação da Base de Dados
from bd import Carros

#Esse módulo do Flask vai subir a nossa API localmente
#Vamos instanciar o modelo Flask na nova variavel app
app = Flask("Carros")

#Metodo 1 - Visualização de dados (GET)
#O que esse metodo vai fazer ?
#Onde vai fazer ?

@app.route("/carrinho", methods = ["GET"])

def get_carros():
    return Carros

#Metodo 1 parte 2 - Visualização de dados por id (GET)

@app.route("/carrinho/<int:id>",methods = ["GET"])

def get_carros_id(id):
    for carro in Carros:
        if carro.get("id") == id:
            return jsonify(carro)

#Metodo 2 - Criar novos registros (POST)
#Verificar os dados que estão sendo passados na requisição e armazenar na nova API
@app.route("/carrinho", methods = ["POST"])
def criar_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            mensagem = "Carro Cadastrado com Sucesso !",
            carrinho = carro
        )
    )


#Metodo 3 - Deletar registros (DELETE)
@app.route("/carrinho/<int:id>", methods= ["DELETE"])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get("id") == id:
            del Carros[indice]
            return jsonify(
                {"mensagem": "Carro excluido !"}
            )

#Metodo 4 - Editar Registros (PUT)
@app.route("/carrinho/<int:id>", methods = ["PUT"])
def editar_carro(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get("id") == id:
            Carros[indice].update(carro_alterado)
            return jsonify(
                Carros[indice]
                )






app.run(port=5000, host= "localhost", debug = True)

