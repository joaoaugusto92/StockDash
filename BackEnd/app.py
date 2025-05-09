from flask import Flask
from controller.cliente_controller import ClienteController
from service.cliente_service import ClienteService

app = Flask(__name__)

# Inicializando as camadas
cliente_service = ClienteService()
cliente_controller = ClienteController(cliente_service)

@app.route('/clientes/', methods=['POST'])
def criar_cliente():
    return cliente_controller.criar()

@app.route('/clientes/<int:id>', methods=['GET'])
def buscar_cliente(id):
    return cliente_controller.buscar(id)

@app.route('/clientes/', methods=['GET'])
def listar_clientes():
    return cliente_controller.listar()

@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    return cliente_controller.excluir(id)

if __name__ == '__main__':
    app.run(debug=True)
