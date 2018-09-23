import pygame
from Tabuleiro import Tabuleiro

pygame.init()

tela = pygame.display.set_mode((1024,768))
fim = False
mouseEsquerdo = 1


tabuleiroJogo = Tabuleiro()
print(tabuleiroJogo.estado)

while not fim:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == mouseEsquerdo:
            print("Clique esquerdo - posição (%d,%d)" % evento.pos)

        pygame.display.flip()