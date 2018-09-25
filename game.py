import pygame
import os
from Tabuleiro import Tabuleiro

pygame.init()

tela = pygame.display.set_mode((1024,768))
fim = False
mouseEsquerdo = 1


tabuleiroJogo = Tabuleiro()
print(tabuleiroJogo.estado)

bg = pygame.image.load(os.path.join("assets", "sprites", "background.png"))

while not fim:
    tela.blit(tabuleiroJogo.sprite, (0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == mouseEsquerdo:
            print("Clique esquerdo - posição (%d,%d)" % evento.pos)
            print("Clique no tabuleiro - %s " % tabuleiroJogo.mapeiaClique(evento.pos[0], evento.pos[1]))

        pygame.display.flip()
