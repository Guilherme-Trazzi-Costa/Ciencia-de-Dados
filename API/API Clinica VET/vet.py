from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask("clientes")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Senai%40134@127.0.0.1/clinicavetbd"

mybd = SQLAlchemy(app)

class Clientes(mybd.Model):
    __tablename__ = "tb_clientes"
    id_cliente = mybd.Column(mybd.Integer, primary_key=True)
    nome = mybd.Column(mybd.String(255))
    endereco = mybd.Column(mybd.String(255))
    telefone = mybd.Column(mybd.String(30))


    def to_json(self):
        return{
            "id_cliente": self.id_cliente,
            "nome": self.nome,
            "endereco": self.endereco,
            "telefone": self.telefone
        }
    


#GET
@app.route("/clientes", methods = ["GET"])
def seleciona_cliente():
    cliente_selecionado = Clientes.query.all()
    cliente_json = [cliente.to_json()
                    for cliente in cliente_selecionado]
    return gera_resposta(200, "clientes", cliente_json)


#GET (Por id)
@app.route("/clientes/<id_cliente_pam>", methods=["GET"])
def seleciona_cliente_id(id_cliente_pam):
    cliente_selecionado = Clientes.query.filter_by(id_cliente=id_cliente_pam).first()
    cliente_json = cliente_selecionado.to_json()

    return gera_resposta(200, cliente_json, "Cliente encontrado!")


#POST
@app.route("/clientes", methods = ["POST"])
def criar_cliente():
    requisicao = request.get_json()

    try:
        cliente = Clientes(
            id_cliente = requisicao["id_cliente"],
            nome = requisicao["nome"],
            endereco = requisicao["endereco"],
            telefone = requisicao["telefone"]

        )

        mybd.session.add(cliente)

        mybd.session.commit()

        return gera_resposta(201, cliente.to_json(), "Criado com Sucesso !")
    
    except Exception as e:
        print("Erro", e)

        return gera_resposta(400, {}, "Erro ao cadastrar!")


#DELETE

@app.route("/clientes/<id_cliente_pam>", methods=["DELETE"])
def deleta_cliente(id_cliente_pam):
    cliente = Clientes.query.filter_by(id_cliente = id_cliente_pam).first()

    try:
        mybd.session.delete(cliente)

        mybd.session.commit()

        return gera_resposta(200, cliente.to_json(), "Deletado com Sucesso !")
    
    except Exception as e:
        print("Erro", e)
        return gera_resposta(400, {}, "Erro ao Deletar")


#PUT
@app.route("/clientes/<id_cliente_pam>", methods = ["PUT"])
def atualiza_carro(id_cliente_pam):
    cliente = Clientes.query.filter_by(id_cliente = id_cliente_pam).first()
    requisicao = request.get_json()

    try:
        if("nome" in requisicao):
            cliente.nome = requisicao["nome"]
        if("endereco" in requisicao):
            cliente.endereco = requisicao["endereco"]
        if("telefone" in requisicao):
            cliente.telefone = requisicao["telefone"]

        mybd.session.add(cliente)

        mybd.session.commit()

        return gera_resposta(200, cliente.to_json(), "Cliente Atualizado")
    
    except Exception as e:
        print("Erro", e)
        return gera_resposta(400, {}, "Erro ao atualizar!")




#RESPOSTA
def gera_resposta(status, conteudo, mensagem=False):
    body = {}
    body["Lista Clientes"] = conteudo
    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")

app.run(port=5000, host="localhost", debug=True)