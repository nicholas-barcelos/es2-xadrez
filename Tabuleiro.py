import pygame
import os
from MaquinaRegras import MaquinaRegras

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
    pecaSelecionada = " "
    xSelecionado = None
    ySelecionado = None
    dimensao = 400
    casa = dimensao // 8
    offsetX = 16
    offsetY = 40

    def __init__(self):
        pass

    def destroi(self):
        print("Destruir")

    def inverte(self):
        print("Inverte")

    def manipulaClique(self, x, y):
        pecaClicada = self.estado[x][y]
        print("peca clicada: ", pecaClicada)
        print("peca selec: ", self.pecaSelecionada)

        if(pecaClicada.isupper()):
            self.pecaSelecionada = pecaClicada
            self.xSelecionado = x
            self.ySelecionado = y
            return False
        elif(self.pecaSelecionada != " "):
            return self.movePeca(x, y)
        return False

    def removePeca(self, x, y):
        self.estado[x][y] = " "

    def trocarPeca(self, x, y):
        print("Trocar posicao")

    def retornaPeca(self, x, y):
        print("Nao lembro")

    def movePeca(self, xDestino, yDestino):
        if (MaquinaRegras.validaMovimentacao(self.xSelecionado, self.ySelecionado, xDestino, yDestino, self.estado)):
            self.estado[xDestino][yDestino] = self.estado[self.xSelecionado][self.ySelecionado]
            self.estado[self.xSelecionado][self.ySelecionado] = " "
            self.pecaSelecionada = " "
            print("Pode Movimntar")
            return True
        print("Não pode Movimntar")
        return False

