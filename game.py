import pygame
import os
from Tabuleiro import Tabuleiro

pygame.init()

tela = pygame.display.set_mode((640,480))
fim = False
mouseEsquerdo = 1


tabuleiroJogo = Tabuleiro()
print(tabuleiroJogo.estado)

peoes_pretos = [tabuleiroJogo.desenhaPeca(1, x, "preto_peao.png") for x in range(8)]
peoes_brancos= [tabuleiroJogo.desenhaPeca(6, x, "branco_peao.png") for x in range(8)]

nomes_pretas = ["preto_torre.png", "preto_cavalo.png", "preto_bispo.png", "preto_rei.png", "preto_rainha.png", "preto_bispo.png", "preto_cavalo.png", "preto_torre.png"]
nomes_brancas = ["branco_torre.png", "branco_cavalo.png", "branco_bispo.png", "branco_rainha.png", "branco_rei.png", "branco_bispo.png", "branco_cavalo.png", "branco_torre.png"]

pecas_pretas = [tabuleiroJogo.desenhaPeca(0, x, nomes_pretas[x]) for x in range(8)]
pecas_brancas = [tabuleiroJogo.desenhaPeca(7, x, nomes_brancas[x]) for x in range(8)]

todas_pecas = pecas_pretas + peoes_pretos + peoes_brancos + pecas_brancas

while not fim:
    tela.blit(tabuleiroJogo.sprite, (0, 0))
    for peca in todas_pecas:
        tela.blit(peca[2], (peca[0], peca[1]))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == mouseEsquerdo:
            print("Clique esquerdo - posição (%d,%d)" % evento.pos)
            print("Clique no tabuleiro - %s " % tabuleiroJogo.mapeiaClique(evento.pos[0], evento.pos[1]))

        pygame.display.flip()