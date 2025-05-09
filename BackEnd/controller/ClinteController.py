from flask import jsonify, request
from service.cliente_service import ClienteService

class ClienteController:
    def __init__(self, cliente_service: ClienteService):
        self.cliente_service = cliente_service

    def criar(self):
        data = request.get_json()
        id = data.get("id")
        nome = data.get("nome")
        email = data.get("email")
        whatsapp = data.get("whatsapp")
        instagram = data.get("instagram")
        pontos = data.get("pontos", 0)

        try:
            self.cliente_service.criar_cliente(id, nome, email, whatsapp, instagram, pontos)
            return jsonify({"message": f"Cliente {nome} criado com sucesso!"}), 201
        except ValueError as e:
            return jsonify({"message": str(e)}), 400

    def buscar(self, id):
        cliente = self.cliente_service.buscar_cliente(id)
        if cliente:
            return jsonify({
                "id": cliente.id,
                "nome": cliente.nome,
                "email": cliente.email,
                "whatsapp": cliente.whatsapp,
                "instagram": cliente.instagram,
                "pontos": cliente.pontos
            }), 200
        return jsonify({"message": "Cliente não encontrado"}), 404

    def listar(self):
        clientes = self.cliente_service.listar_clientes()
        return jsonify([{
            "id": cliente.id,
            "nome": cliente.nome,
            "email": cliente.email,
            "whatsapp": cliente.whatsapp,
            "instagram": cliente.instagram,
            "pontos": cliente.pontos
        } for cliente in clientes]), 200

    def excluir(self, id):
        try:
            self.cliente_service.excluir_cliente(id)
            return jsonify({"message": f"Cliente {id} excluído com sucesso!"}), 200
        except Exception as e:
            return jsonify({"message": str(e)}), 400

