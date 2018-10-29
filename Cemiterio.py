import pygame
import os

'''
Fonte:
Aseprite Remix by zephram
https://creativecommons.org/licenses/by-nc/3.0/
'''

class Cemiterio:
    #Dicionário de peças, "nome":qtd
    instancia = None
    covas = None
    #covasBrancas = None
    #covasPretas = None
    # pra poder imprimir os amiguinhos no local certo
    qtd = 0

    def __init__(self):
        self.covas = {
            "brancas": {},
            "pretas": {}
        }


    @staticmethod
    def pegaInstancia():
        if not Cemiterio.instancia:
            Cemiterio.instancia = Cemiterio()
        return Cemiterio.instancia

    def adicionaPeca(self, peca, tabuleiro):
        self.qtd+=1
        if tabuleiro.pegaJogadorAtual() == 1:
            if peca in self.covas['brancas']:
                self.covas['brancas'][peca] += 1
            else:
                self.covas['brancas'][peca] = 1
        else:
            if peca in self.covas['pretas']:
                self.covas['pretas'][peca] += 1
            else:
                self.covas['pretas'][peca] = 1


    def removePeca(self, peca, tabuleiro):
        if peca not in self.covas['brancas'] and peca not in self.covas['pretas']:
            print("Esta peca não está no cemitério. Pare.")
            return

        if tabuleiro.pegaJogadorAtual() == 1:
            if peca in self.covas['brancas']:
                self.covas['brancas'][peca] -= 1
        else:
            if peca in self.covas['brancas']:
                self.covas['brancas'][peca] -= 1