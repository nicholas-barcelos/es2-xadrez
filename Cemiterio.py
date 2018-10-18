import pygame
import os
# from MaquinaRegras import MaquinaRegras
from Interface import Interface

'''
Fonte:
Aseprite Remix by zephram
https://creativecommons.org/licenses/by-nc/3.0/
'''

class Cemiterio:

    #Dicionário de peças, "nome":qtd
    covas = {}
    interface = Interface()
    # pra poder imprimir os amiguinhos no local certo
    qtdAlto = -1
    qtdBaixo = -1


    def __init__(self):
        pass

    def adicionaPeca(self, peca):
        if peca.isupper():
            self.qtdAlto+=1
        else:
            self.qtdBaixo+=1

        if peca in self.covas:
            self.covas[peca] += 1
            self.interface.desenhaCemiterio(peca, True)
            #aumenta o contador embaixo da peça
        else:
            self.covas[peca] = 1
            sprite = pygame.image.load(os.path.join("assets", "sprites", peca)) #acho que essa funcao nao vai prestar pra pintar no cemiterio
            self.interface.desenhaCemiterio(peca, False)
            #cria um contador embaixo da peça

    def removePeca(self, peca):
        if peca in self.covas:
            self.covas[peca] -= 1
        else:
            print("Esta peca não está no cemitério. Pare.")