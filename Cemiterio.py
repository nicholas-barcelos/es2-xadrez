import pygame
import os
from MaquinaRegras import MaquinaRegras
from Interface import Inteface

'''
Fonte:
Aseprite Remix by zephram
https://creativecommons.org/licenses/by-nc/3.0/
'''

class Cemiterio:

    #Dicionário de peças, "nome":qtd
    covas = {}

    # pra poder imprimir os amiguinhos no local certo
    qtdAlto = -1
    qtdBaixo = -1


    def __init__(self):
        pass

    def adicionaPeca(self, peca):
        if peca.isupper():
            qtdAlto++
        else:
            qtdBaixo++

        if peca in covas:
            covas[peca] = covas[peca] + 1
            desenhaCemiteroi(peca, True)
            #aumenta o contador embaixo da peça
        else:
            covas[peca] = 1
            sprite = pygame.image.load(os.path.join("assets", "sprites", peca)) #acho que essa funcao nao vai prestar pra pintar no cemiterio
            desenhaCemiteroi(peca, False)
            #cria um contador embaixo da peça

    def removePeca(self, peca):
        if peca in covas:
            covas[peca] = covas[peca] - 1
        else:
            print("Esta peca não está no cemitério. Pare.")