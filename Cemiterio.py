import pygame
import os

'''
Fonte:
Aseprite Remix by zephram
https://creativecommons.org/licenses/by-nc/3.0/
'''

class Cemiterio:

    #Dicionário de peças, "nome":qtd
    covas = None
    # pra poder imprimir os amiguinhos no local certo
    qtd = 0

    def __init__(self):
        self.covas = {}

    def adicionaPeca(self, peca):
        self.qtd+=1
        if peca in self.covas:
            self.covas[peca] += 1
        else:
            self.covas[peca] = 1

    def removePeca(self, peca):
        if peca in self.covas:
            self.covas[peca] -= 1
        else:
            print("Esta peca não está no cemitério. Pare.")