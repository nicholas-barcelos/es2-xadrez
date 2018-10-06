import pygame
import os
from MaquinaRegras import MaquinaRegras
from Interface import Inteface

class Cemiterio:

    #Dicionário de peças, "nome":qtd, 
    covas = {}

    def __init__(self):
        pass

    def adicionaPeca(self, peca):
        if peca in covas:
            covas[peca] = covas[peca] + 1
            #aumenta o contador embaixo da peça
        else:
            covas[peca] = 1
            desenhaPeca(9,0, peca) #acho que essa funcao nao vai prestar pra pintar no cemiterio
            #cria um contador embaixo da peça

    def removePeca(self, peca):
        if peca in covas:
            covas[peca] = covas[peca] - 1
        else:
            print("Esta peca não está no cemitério. Pare.")