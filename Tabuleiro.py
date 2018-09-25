import pygame
import os
# from MaquinaRegras import validaMovimentacao

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

    def __init__(self, tela):
        self.sprite = pygame.image.load(os.path.join("assets", "sprites", "background.png"))
        tela.blit(self.sprite, (0, 0))
            
    def cria(tela):
        print("Criar")
        bsoldado = pygame.image.load(os.path.join("assets","sprites","bsoldier.png"))
        wsoldado = pygame.image.load(os.path.join("assets","sprites","wsoldier.png"))
        
        x = 20
        y = 30
        for i in range (7):
            print("tentando imprimir soldado ")
            tela.blit(bsoldado, (x, y))
            tela.blit(wsoldado, (x, y+60))
            x +=20

    def destroi(self):
        print("Destruir")

    def inverte(self):
        print("Inverte")

    def mapeiaClique(self, x, y):
        i = (x - self.offsetX)//self.casa
        j = (y - self.offsetY)//self.casa
        if i > 7 or j > 7:
            return "casa inválida"
        return self.estado[j][i]
    
    def removePeca(self, x, y):
        self.estado[x][y] = " "

    def trocarPeca(self, x, y):
        print("Trocar posicao")

    def retornaPeca(self, x, y):
        print("Nao lembro")

    
"""
    def movePeca(self, xOrigem,yOrigem,xDestino,yDestino):
        peca = self.estado[xOrigem][yOrigem]
        if (validaMovimentacao(self.estado, xOrigem, yOrigem, xDestino, yDestino)): #o valida movimento deve avaliar a peca e verificar se o movimento eh valido e possivel
            self.removePeca(xOrigem, yOrigem) #caso o removePeca faca mais que apagar a peca, eh uma boa tirar por aqui msm... soh coloquei por facilidade de manutenção
            self.estado[xDestino][yDestino] = peca
"""
