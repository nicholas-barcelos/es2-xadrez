import os

import pygame

import Tabuleiro as tb

class Interface:
    tabuleiro = None
    tela = None
    dimensao = 400
    casa = dimensao // 8
    offsetX = 16
    offsetY = 40
    instancia = None

    def __init__(self, vertical=480, horizontal=640):
        self.tela = pygame.display.set_mode((horizontal,vertical))
        self.tabuleiro = tb.Tabuleiro.pegaInstancia()
        self.sprite = pygame.image.load(os.path.join("assets", "sprites", "background.png"))

    @staticmethod
    def pegaInstancia():
        if not Interface.instancia:
            Interface.instancia = Interface()
        return Interface.instancia

    #desenha tela do jogo percorrendo o tabuleiro
    def cria(self):
        self.tela.blit(self.sprite, (0, 0))
        estado = self.tabuleiro.estado
        x = estado.__len__()
        for i in range(x):
            y = estado[i].__len__()
            for j in range(y):
                self.desenhaPosicao(j, i)
        self.desenhaCemiterio(self.tabuleiro.cemiterio, self.tabuleiro.pegaJogadorAtual())

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

    #posicao diz se o cemiterio vai ser desenhado em cima ou em baixo... 1 = cima, 2 = baixo
    def desenhaCemiterio(self,cemiterio, posicao):
        x = 455
        yCima = 300
        yBaixo = 70
        cont = 1
        if cemiterio.covas['brancas']:
            for k in cemiterio.covas['brancas'].keys():
                if(cont == 4):
                    yCima += 60
                    x = 455
                self.desenhaPeca(x, yCima, k)
                x+=55
                cont+=1

        x = 455
        cont=1
        if cemiterio.covas['pretas']:
            for k in cemiterio.covas['pretas'].keys():
                if(cont == 4):
                    yBaixo += 60
                    x = 455
                self.desenhaPeca(x, yBaixo, k)
                x+=55
                cont+=1
