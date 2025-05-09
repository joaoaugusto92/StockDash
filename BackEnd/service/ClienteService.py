from repository.cliente_repository import ClienteRepository
from models.cliente import Cliente

class ClienteService:
    def __init__(self):
        self.cliente_repository = ClienteRepository()

    def criar_cliente(self, id, nome, email=None, whatsapp=None, instagram=None, pontos=0):
        if not nome:
            raise ValueError("Nome é obrigatório")
        cliente = Cliente(id=id, nome=nome, email=email, whatsapp=whatsapp, instagram=instagram, pontos=pontos)
        self.cliente_repository.salvar(cliente)

    def buscar_cliente(self, id):
        return self.cliente_repository.buscar_por_id(id)

    def listar_clientes(self):
        return self.cliente_repository.listar()

    def excluir_cliente(self, id):
        self.cliente_repository.excluir(id)

