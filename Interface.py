import os

import pygame

from Tabuleiro import Tabuleiro

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
        self.desenhaCemiterio(self.tabuleiro.cemiterioMaquina, 1)
        self.desenhaCemiterio(self.tabuleiro.cemiterioPlayer, 2)

    #recebe o clique e passa para o tabuleiro manipular
    def mapeiaClique(self, x, y):
        i = (x - self.offsetX)//self.casa
        j = (y - self.offsetY)//self.casa
        print("x = ", x, " y= ", y)
        if i > 7 or j > 7:
            return "casa inválida"
        pecaClicada = self.tabuleiro.estado[j][i]
        if(self.tabuleiro.manipulaClique(j,i)):
            if(pecaClicada != " "):
                print("===PECA ",pecaClicada," CAPTURADA!!=== ")
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
        if(sprite != None):
            self.tela.blit(sprite, (x, y))

    def desenhaPeca(self, x, y, peca):
        sprite = self.imagemPeca(peca)
        self.tela.blit(sprite, (x, y))

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

    """    # peca: peca a ser desenhada
        # qtd: numero a ser desenhado embaixo da peca
        # pos: posicao que a imagemzinha da peca sera desenhada, tipo: linha1: peca1 peca2 peca3
        #                                                              linha2:     peca4 peca5
        #flag: if true, a peca foi desenhada no cemiterio e so e necessario redesenhar o contador embaixo.
    def desenhaCemiterio(self, peca, qtd, pos, flag):
        fonte = pygame.font.Font(os.path.join("assets", "fontes", "aseprite-remix.ttf"), 8)
        text = fonte.render("Qtd: " + str(qtd), True, (0, 0, 0))
        sprite = self.imagemPeca(peca)

        if peca.isupper():
            if flag:
                # Aumenta o contador de cima 
                return
            #desenha na linha de cima
            if (pos<3):
               self.tela.blit(sprite, ((455 + (pos*55)), 304))
            else:
                self.tela.blit(sprite, ((475 + ((pos-3)*60)), 147))
            return
        if peca.islower():
            print("Passou por aqui...")
            if flag:
                # Aumenta o contador de baixo
                return
            if (pos==1):
               self.tela.blit(sprite, (460, 70))
            elif(pos == 2):
                self.tela.blit(sprite, (515, 70))
            elif (pos == 3):
                self.tela.blit(sprite, (570, 70))
            else:
                self.tela.blit(sprite, ((475 + ((pos-3)*60)), 372))
            return
        print("Como você chegou até aqui?")"""

    #posicao diz se o cemiterio vai ser desenhado em cima ou em baixo... 1 = cima, 2 = baixo
    def desenhaCemiterio(self,cemiterio, posicao):
        x = 455
        y = 300
        if (posicao == 1): y = 70
        cont = 1
        for k in cemiterio.covas.keys():
            if(cont == 4):
                y += 60
                x = 455
            self.desenhaPeca(x, y, k)
            x+=55
            cont+=1
