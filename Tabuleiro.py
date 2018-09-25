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

    def __init__(self):
        self.sprite = pygame.image.load(os.path.join("assets", "sprites", "background.png"))
            
    def cria(self, tela):
        # TODO: SIMPLIFICAR PARA CARAMBOLAS ISSO DAQUI
        # codigo estilo dojo que funciona
        tela.blit(self.sprite, (0, 0))
        print("Criar")
        print("Imprimindo soldados...")

        for i in range (8):
            bsoldado = self.desenhaPeca(i, 1, "bsoldier.png")
            wsoldado = self.desenhaPeca(i, 6, "wsoldier.png")
            tela.blit(bsoldado[2], (bsoldado[0], bsoldado[1]))
            tela.blit(wsoldado[2], (wsoldado[0], wsoldado[1]))
        
        btorre1 = self.desenhaPeca(0, 0, "btower.png")
        btorre2 = self.desenhaPeca(7, 0, "btower.png")
        wtorre1 = self.desenhaPeca(0, 7, "wtower.png")
        wtorre2 = self.desenhaPeca(7, 7, "wtower.png")
        tela.blit(btorre1[2], (btorre1[0], btorre1[1]))
        tela.blit(btorre2[2], (btorre2[0], btorre2[1]))
        tela.blit(wtorre1[2], (wtorre1[0], wtorre1[1]))
        tela.blit(wtorre2[2], (wtorre2[0], wtorre2[1]))
        
        # Inicializar Cavalos
        bcavalo1 = self.desenhaPeca(1, 0, "bhorse.png")
        bcavalo2 = self.desenhaPeca(6, 0, "bhorse.png")
        wcavalo1 = self.desenhaPeca(1, 7, "whorse.png")
        wcavalo2 = self.desenhaPeca(6, 7, "whorse.png")
        tela.blit(bcavalo1[2], (bcavalo1[0], bcavalo1[1]))
        tela.blit(bcavalo2[2], (bcavalo2[0], bcavalo2[1]))
        tela.blit(wcavalo1[2], (wcavalo1[0], wcavalo1[1]))
        tela.blit(wcavalo2[2], (wcavalo2[0], wcavalo2[1]))
        
        
        # Inicializar Bispos
        bbispo1 = self.desenhaPeca(2, 0, "bbishop.png")
        bbispo2 = self.desenhaPeca(5, 0, "bbishop.png")
        wbispo1 = self.desenhaPeca(2, 7, "wbishop.png")
        wbispo2 = self.desenhaPeca(5, 7, "wbishop.png")
        tela.blit(bbispo1[2], (bbispo1[0], bbispo1[1]))
        tela.blit(bbispo2[2], (bbispo2[0], bbispo2[1]))
        tela.blit(wbispo1[2], (wbispo1[0], wbispo1[1]))
        tela.blit(wbispo2[2], (wbispo2[0], wbispo2[1]))
        
        brainha = self.desenhaPeca(3, 0, "bqueen.png")
        tela.blit(brainha[2], (brainha[0], brainha[1]))
        wrainha = self.desenhaPeca(4, 7, "wqueen.png")
        tela.blit(wrainha[2], (wrainha[0], wrainha[1]))
        
        brei = self.desenhaPeca(4, 0, "bking.png")
        tela.blit(brei[2], (brei[0], brei[1]))
        wrei = self.desenhaPeca(3, 7, "wking.png")
        tela.blit(wrei[2], (wrei[0], wrei[1]))
        

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
    
    def desenhaPeca(self, i, j, peca):
        x = i * self.casa + self.offsetX
        y = j * self.casa + self.offsetY
        sprite = pygame.image.load(os.path.join("assets", "sprites", peca))
        return (x, y, sprite)
    
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
