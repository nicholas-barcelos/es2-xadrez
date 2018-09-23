class Tabuleiro:
    estado = [
        ["t", "h", "b", "k", "q", "b", "h", "t"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["T", "H", "B", "Q", "K", "B", "H", "T"]
    ]

    def __init__(self):
        pass

    def cria(self):
        print("Criar")

    def destroi(self):
        print("Destruir")

    def inverte(self):
        print("Inverte")

    def movePeca(self, xOrigem,yOrigem,xDestino,yDestino):
        print("mover")

    def removePeca(self, x, y):
        print("remover")

    def trocarPeca(self, x, y):
        print("Trocar posicao")

    def retornaPeca(self, x, y):
        print("Nao lembro")