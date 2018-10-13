import os

import pygame

from Tabuleiro import Tabuleiro
# from Cemiterio import Cemiterio

class Interface:
    tabuleiro = None
    tela = None
    dimensao = 400
    casa = dimensao // 8
    offsetX = 16
    offsetY = 40

    def __init__(self, vertical=480, horizontal=640):
        self.tela = pygame.display.set_mode((horizontal,vertical))
        self.tabuleiro = Tabuleiro()
        self.sprite = pygame.image.load(os.path.join("assets", "sprites", "background.png"))

    #desenha tela do jogo percorrendo o tabuleiro
    def cria(self):
        self.tela.blit(self.sprite, (0, 0))
        estado = self.tabuleiro.estado
        x = estado.__len__()
        for i in range(x):
            y = estado[i].__len__()
            for j in range(y):
                self.desenhaPosicao(j, i)

    #recebe o clique e passa para o tabuleiro manipular
    def mapeiaClique(self, x, y):
        i = (x - self.offsetX)//self.casa
        j = (y - self.offsetY)//self.casa
        if i > 7 or j > 7:
            return "casa inválida"
        if(self.tabuleiro.manipulaClique(j,i)):
            print("Retornou True")
            self.cria()
        print("Retornou False")
        return self.tabuleiro.estado[j][i]

    # retorna imagem da peça baseado no nome lógico dela
    def imagemPeca(self, peca):
        imagem = None
        if(peca == " ") : return
        elif( peca == "p") : imagem = "bsoldier.png"
        elif (peca == "P") : imagem = "wsoldier.png"
        elif (peca == "t") : imagem = "btower.png"
        elif (peca == "T") : imagem = "wtower.png"
        elif (peca == "h") : imagem = "bhorse.png"
        elif (peca == "H"):  imagem = "whorse.png"
        elif (peca == "b") : imagem = "bbishop.png"
        elif (peca == "B") : imagem = "wbishop.png"
        elif (peca == "k") : imagem = "bking.png"
        elif (peca == "K") : imagem = "wking.png"
        elif (peca == "q") : imagem = "bqueen.png"
        elif (peca == "Q") : imagem = "wqueen.png"
        return pygame.image.load(os.path.join("assets", "sprites", imagem))

    #desenha a peca na posicao correspondente
    def desenhaPosicao(self, i, j):
        peca = self.tabuleiro.estado[j][i]

        x = i * self.casa + self.offsetX
        y = j * self.casa + self.offsetY
        sprite = self.imagemPeca(peca)
        self.tela.blit(sprite, (x, y))

    def desenhaPeca(self, i, j, peca):
        x = i * self.casa + self.offsetX
        y = j * self.casa + self.offsetY
        sprite = self.imagemPeca(peca)
        return (x, y, sprite)

    def mostrar(self):
        print()

    def atualizar(self):
        print()

    def telaInicio(self):
        print()

    def telaCheque(self):
        print()

    def telaDerrota(self):
        print()

    def telaVitoria(self):
        print()

    def peca(self):
        print()

    def tabuleiro(self):
        print()

        # peca: peca a ser desenhada
        # qtd: numero a ser desenhado embaixo da peca
        # pos: posicao que a imagemzinha da peca sera desenhada, tipo: linha1: peca1 peca2 peca3
        #                                                              linha2:     peca4 peca5
        #flag: if true, a peca foi desenhada no cemiterio e so e necessario redesenhar o contador embaixo.
    def desenhaCemiterio(self, peca, qtd, pos, flag):
        fonte = pygame.font.Font(os.path.join("assets", "fontes", "aseprite-remix.ttf"), 8)
        text = fonte.render("Qtd: " + str(qtd), True, (0, 0, 0))
        if peca.isupper():
            if flag:
                # Aumenta o contador de cima 
                return
            sprite = self.imagemPeca(peca)
            #desenha na linha de cima
            if (pos<3):
               self.tela.blit(sprite, ((455 + (pos*55)), 304))
            else:
                self.tela.blit(sprite, ((475 + ((pos-3)*60)), 147))
            return
        if peca.islower():
            if flag:
                # Aumenta o contador de baixo
                return
            if (pos<3):
               self.tela.blit(sprite, ((455 + (pos*55)), 304))
            else:
                self.tela.blit(sprite, ((475 + ((pos-3)*60)), 372))
            return
        print("Como você chegou até aqui?")

