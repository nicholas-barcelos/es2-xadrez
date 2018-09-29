import pygame
import os
#from Tabuleiro import Tabuleiro
from Interface import Interface

pygame.init()

#tela = pygame.display.set_mode((640,480))

fim = False
mouseEsquerdo = 1

bg = pygame.image.load(os.path.join("assets", "sprites", "background.png"))

#tabuleiroJogo = Tabuleiro()
#tabuleiroJogo.cria(tela)

interface = Interface(640, 480)
interface.cria()

#print(tabuleiroJogo.estado)

while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == mouseEsquerdo:
            print("Clique esquerdo - posição (%d,%d)" % evento.pos)
            print("Clique no tabuleiro - %s " % interface.mapeiaClique(evento.pos[0], evento.pos[1]))

        pygame.display.flip()
