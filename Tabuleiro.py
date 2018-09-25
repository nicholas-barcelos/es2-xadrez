import pygame
import os
class Tabuleiro:
    estado = [
        ["t", "h", "b", "k", "q", "b", "h", "t"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["T", "H", "B", "Q", "K", "B", "H", "T"]
    ]
    dimensao = 400
    casa = dimensao // 8
    offsetX = 16
    offsetY = 40

    def __init__(self):
        self.sprite = pygame.image.load(os.path.join("assets", "sprites", "background.gif"))

    def cria(self):
        print("Criar")

    def destroi(self):
        print("Destruir")

    def inverte(self):
        print("Inverte")

    def mapeiaClique(self, x, y):
        i = (x - self.offsetX) // self.casa
        j = (y - self.offsetY) // self.casa
        if i < 0 or i > 7 or j < 0 or j > 7:
            return "casa inválida"
        return self.estado[j][i]

    def desenhaPeca(self, i, j, peca):
        x = i * self.casa + self.offsetX
        y = j * self.casa + self.offsetY
        sprite = pygame.image.load(os.path.join("assets", "sprites", peca))
        return (y, x, sprite)



    def movePeca(self, xOrigem,yOrigem,xDestino,yDestino):
        print("mover")

    def removePeca(self, x, y):
        print("remover")

    def trocarPeca(self, x, y):
        print("Trocar posicao")

    def retornaPeca(self, x, y):
        print("Nao lembro")