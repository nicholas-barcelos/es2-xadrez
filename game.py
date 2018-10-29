import pygame
import os
from Interface import Interface

pygame.init()

fim = False
mouseEsquerdo = 1

bg = pygame.image.load(os.path.join("assets", "sprites", "background.png"))

interface = Interface.pegaInstancia()
interface.cria()

while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == mouseEsquerdo:
            print("Clique esquerdo - posição (%d,%d)" % evento.pos)
            print("Clique no tabuleiro - %s " % interface.mapeiaClique(evento.pos[0], evento.pos[1]))
            print("estado tabuleiro\n", str(interface.tabuleiro))

        pygame.display.flip()
