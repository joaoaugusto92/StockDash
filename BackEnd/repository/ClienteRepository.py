import psycopg2
from database.connection import get_db_connection
from models.cliente import Cliente

class ClienteRepository:
    def __init__(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    def salvar(self, cliente: Cliente):
        query = """
        INSERT INTO clientes (id, nome, email, whatsapp, instagram, pontos)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (cliente.id, cliente.nome, cliente.email, cliente.whatsapp, cliente.instagram, cliente.pontos))
        self.conn.commit()

    def buscar_por_id(self, id: int):
        self.cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        row = self.cursor.fetchone()
        if row:
            return Cliente(*row)
        return None

    def listar(self):
        self.cursor.execute("SELECT * FROM clientes")
        rows = self.cursor.fetchall()
        return [Cliente(*row) for row in rows]

    def excluir(self, id: int):
        self.cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        self.conn.commit()

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()

