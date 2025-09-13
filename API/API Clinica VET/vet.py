from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json



#Tabela Clientes
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


#--------------------------------------------------------------------------------------------

#Chave Estrangeira
#id_cliente = mybd.Column(mybd.Integer, mybd.ForeignKey("tb_clientes.id_cliente"), nullable = False)

#Tabela Pets


class Pets(mybd.Model):
    __tablename__ = "tb_pets"
    id_pet = mybd.Column(mybd.Integer, primary_key = True)
    nome = mybd.Column(mybd.String(255))
    tipo = mybd.Column(mybd.String(255))
    raca = mybd.Column(mybd.String(255))
    data_nascimento = mybd.Column(mybd.String(255))
    id_clienteP = mybd.Column(mybd.Integer, mybd.ForeignKey("tb_clientes.id_clienteP"), nullable = False)

    def to_json_pets(self):
        return{
            "id_pet": self.id_pet,
            "nome": self.nome,
            "tipo":self.tipo,
            "raca": self.raca,
            "data_nascimento": str(self.data_nascimento),
            "id_clienteP": self.id_clienteP

        }

#--------------------------------------------------------------
#GET

@app.route("/pets", methods = ["GET"])

def seleciona_pet():
    pet_selecionado = Pets.query.all()
    pet_json = [pet.to_json_pets()
                for pet in pet_selecionado]
    return gera_resposta(200, "pets", pet_json)


#---------------------------------------------------------------
#GET por id

@app.route("/pets/<id_pet_pam>", methods = ["GET"])
def seleciona_pet_id(id_pet_pam):
    pet_selecionado = Pets.query.filter_by(id_pet = id_pet_pam).first()
    pet_json = pet_selecionado.to_json_pets()

    return gera_resposta(200, pet_json, "Pet Encontrado!")


#--------------------------------------------------------------
# POST

@app.route("/pets", methods = ["POST"])
def criar_pet():
    requisicao = request.get_json()

    try:
        pet = Pets(
            id_pet =requisicao["id_pet"],
            nome = requisicao["nome"],
            tipo = requisicao["tipo"],
            raca = requisicao["raca"],
            data_nascimento = requisicao["data_nascimento"],
            id_clienteP = requisicao["id_clienteP"]
        )

        mybd.session.add(pet)

        mybd.session.commit()

        return gera_resposta(201, pet.to_json_pets(), "Criado com Sucesso!")
    
    except Exception as e:
        print("Erro", e)

        return gera_resposta(400, {}, "Erro ao cadastrar!")
    
    #-----------------------------------------------------------
    #DELETE

@app.route("/pets/<id_pet_pam>", methods = ["DELETE"])
def deleta_pet(id_pet_pam):
    pet = Pets.query.filter_by(id_pet = id_pet_pam).first()

    try:
        mybd.session.delete(pet)

        mybd.session()

        return gera_resposta(200, pet.to_json_pets(), "Deletado com Sucesso")

    except Exception as e:
        print("Erro", e)
        return gera_resposta(400, {}, "Erro ao Deletar!")
    
#-------------------------------------------------------------------
#PUT
@app.route("/pets/<id_pet_pam>", methods= ["PUT"])
def atualiza_pet(id_pet_pam):
    pet = Pets.query.filter_by(id_pet = id_pet_pam).first()
    requisicao = request.get_json()

    try:
        if("nome" in requisicao):
            pet.nome = requisicao["nome"]
        if("tipo" in requisicao):
            pet.tipo = requisicao["tipo"]
        if("raca" in requisicao):
            pet.raca = requisicao["raca"]
        if("data_nascimento" in requisicao):
            pet.data_nascimento = requisicao["data_nascimento"]

        mybd.session.add(pet)

        mybd.session.commit()

        return gera_resposta(200, pet.to_json_pet(), "Pet atualizado !")
    
    except Exception as e:
        print("Erro", e)
        return gera_resposta(400, {}, "Erro ao atualizar!")
    




#RESPOSTA
def gera_resposta(status, conteudo, mensagem=False):
    body = {}
    body["Lista"] = conteudo
    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")

app.run(port=5000, host="localhost", debug=True)