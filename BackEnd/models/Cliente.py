class Cliente:
    def __init__(self, id, nome, email=None, whatsapp=None, instagram=None, pontos=0):
        self.id = id
        self.nome = nome
        self.email = email
        self.whatsapp = whatsapp
        self.instagram = instagram
        self.pontos = pontos
