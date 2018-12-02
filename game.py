import pygame
import os
from Interface import Interface

pygame.init()


fim = False
mouseEsquerdo = 1

telaInicial = True

# coisas de login
tela = pygame.display.set_mode((640,480))
sprite = pygame.image.load(os.path.join("assets", "sprites", "login1.png"))
tela.blit(sprite, (0, 0))

while telaInicial and not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == mouseEsquerdo:
            telaInicial = False

        pygame.display.flip()


#entrando no jogo
# bg = pygame.image.load(os.path.join("assets", "sprites", "background.png"))
interface = Interface.pegaInstancia()
interface.cria()

# game loop
while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == mouseEsquerdo:
            print("Clique esquerdo - posição (%d,%d)" % evento.pos)
            print("Clique no tabuleiro - %s " % interface.mapeiaClique(evento.pos[0], evento.pos[1]))
            print("Clique no botão de help? - %s " % interface.telaAjuda(evento.pos[0], evento.pos[1]))
            print("estado tabuleiro\n", str(interface.tabuleiro))

        pygame.display.flip()
