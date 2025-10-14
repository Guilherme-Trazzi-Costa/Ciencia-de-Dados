#SQL_ALCHEMY

#pip install flask_sqlalchemy
#pip install pymysql
#pip install mysqlclient
#Permite Conexão da API com o banco de dados
#Flask permite criação de API com Python

#Response e Request -> requisição
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask("carros")

#Rastrear modificaç~eos realizadas
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#Configuração de conexão com o banco
#1-Usuario, 2-Senha, 3 - localhost, 4 - nome do banco


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Senai%40134@127.0.0.1/db_carro"

mybd = SQLAlchemy(app)

#Classe para definir o modelo dos dados que correspondem a tabela do banco de dados

class Carros(mybd.Model):
    __tablename__ = "tb_carro"
    id_carro = mybd.Column(mybd.Integer, primary_key=True)
    marca = mybd.Column(mybd.String(100))
    modelo = mybd.Column(mybd.String(100))
    ano = mybd.Column(mybd.String(100))
    cor = mybd.Column(mybd.String(100))
    valor = mybd.Column(mybd.String(100))
    numero_Vendas = mybd.Column(mybd.String(100))

#Esse metodo é usado para converter o objeto em json
    def to_json(self):
        return{
            "id_carro": self.id_carro,
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano,
            "cor": self.cor,
            "valor": float(self.valor),
            "numero_Vendas":self.numero_Vendas
        }

#-------------------------------------------------------------

#Metodo 1 - GET

@app.route("/carros", methods = ["GET"])

def seleciona_carro():
    carro_selecionado = Carros.query.all()
    #Executa consulta no banco de dados (SELECT * FROM tb_carros)
    carro_json = [carro.to_json()
                  for carro in carro_selecionado]
    return gera_resposta(200, "carros", carro_json)


#----------------------------------------------------------------
#Metodo 2 - (GET por id )


@app.route("/carros/<id_carro_pam>", methods=["GET"])
def seleciona_carro_id(id_carro_pam):
    carro_selecionado = Carros.query.filter_by(id_carro=id_carro_pam).first()
    #SELECT * FROM tb_carro WHERE id_carro = 5
    carro_json = carro_selecionado.to_json()

    return gera_resposta(200, carro_json, "Carro encontrado!")


#-----------------------------------------------------------------
#Metodo 3 - POST

@app.route("/carros", methods=["POST"])
def criar_carro():
    requisicao = request.get_json()

    try:
        carro = Carros(
            id_carro = requisicao["id_carro"],
            marca = requisicao["marca"],
            modelo = requisicao["modelo"],
            ano = requisicao["ano"],
            valor = requisicao["valor"],
            cor = requisicao["cor"],
            numero_Vendas = requisicao["numero_Vendas"]
        )
#Adiciona novo registro ao banco
        mybd.session.add(carro)

#Salva novo registro no banco
        mybd.session.commit()


        return gera_resposta(201, carro.to_json(), "Criado com Sucesso !")


    except Exception as e:
        print("Erro", e)

        return gera_resposta(400, {}, "Erro ao Cadastrar!")


#----------------------------------------------------------------
#Metodo 4 - DELETE

@app.route("/carros/<id_carro_pam>", methods=["DELETE"])
def deleta_carro(id_carro_pam):
    carro = Carros.query.filter_by(id_carro = id_carro_pam).first()

    try:
        mybd.session.delete(carro)

        mybd.session.commit()

        return gera_resposta(200, carro.to_json(), "Deletado com Sucesso !")
    
    except Exception as e:
        print("ERRO", e)
        return gera_resposta(400, {}, "Erro ao Deletar!")

#----------------------------------------------------------------
#Metodo 5 - PUT
@app.route("/carros/<id_carro_pam>", methods=["PUT"])
def atualiza_carro(id_carro_pam):
    carro = Carros.query.filter_by(id_carro = id_carro_pam).first()
    requisicao = request.get_json()

    try:
        if("marca" in requisicao):
            carro.marca = requisicao["marca"]
        if("modelo" in requisicao):
            carro.modelo = requisicao["modelo"]
        if("ano" in requisicao):
            carro.ano = requisicao["ano"]
        if("valor" in requisicao):
            carro.valor = requisicao["valor"]
        if("cor" in requisicao):
            carro.cor = requisicao["cor"]
        if("numero_Vendas" in requisicao):
            carro.numero_Vendas = requisicao["numero_Vendas"]

        mybd.session.add(carro)

        mybd.session.commit()

        return gera_resposta(200, carro.to_json(), "Carro Atualizado com Sucesso !")
    
    except Exception as e:
        print("Erro", e)
        return gera_resposta(400, {}, "Erro ao atualizar!")
        

#-----------------------------------------------------------------
#RESPOSTA PADRÃO
    # - status (200, 201)
    # Conteudo
    # Mensagem (opcional)

def gera_resposta(status, conteudo, mensagem=False):
    body = {}
    body["Lista Carros"] = conteudo
    if (mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")
#dumps converte dicionario criado(body) em json


app.run(port=500, host="localhost", debug=True)

