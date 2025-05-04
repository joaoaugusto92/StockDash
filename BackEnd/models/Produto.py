class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto[ID: {self.id}, Nome: {self.nome}, Preço: R${self.preco:.2f}]"