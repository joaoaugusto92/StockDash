#requisiçoes web.

from flask import Flask, jsonify, Response, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

produtos = [
    {
        "id": 1,
        "nome": "Cem anos de solidão",
        "preco": 30.0
    },
    {
        "id": 2,
        "nome": "Assassinato no expresso do oriente",
        "preco": 25.0
    }
]

@app.get("/produtos")
def allProdutos():
    return jsonify(produtos)

@app.get("/produtos/<int:id>")
def produto(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)
    return Response(json.dumps({"error": "Produto não encontrado"}), status=404, mimetype='application/json')

@app.post("/produtos")
def addProduto():
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    last_id = produtos[-1]["id"]
    novo_produto = {
        "id": last_id + 1,
        "nome": nome,
        "preco": preco
    }
    produtos.append(novo_produto)
    return jsonify(novo_produto), 201

@app.put("/produtos/<int:id>")
def updateProduto(id):

    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")

    for produto in produtos:
        if produto["id"] == id:
            produto["nome"] = nome
            produto["preco"] = preco
            return jsonify(produto)
    return Response(json.dumps({"error": "Produto não encontrado"}), status=404, mimetype='application/json')

@app.delete("/produtos/<int:id>")
def deleteProduto(id):
    for produto in produtos:
        if produto["id"] == id:
            produtos.remove(produto)
            return Response(json.dumps({"message": "Produto removido com sucesso"}), status=200, mimetype='application/json')
    return Response(json.dumps({"error": "Produto não encontrado"}), status=404, mimetype='application/json')