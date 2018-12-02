import Heuristica as hr
import MaquinaRegras as mr

def avaliaEstado(tabuleiro):
    valorTabuleiro = 0
    for i in range(8):
        for j in range(8):
            valorTabuleiro += hr.Heuristica.pegaValorPeca(tabuleiro.estado[i][j], i, j)
    return valorTabuleiro


def pegaMovimentos(tabuleiro, jogadorMax):
    #vai pegar proximos estados possiveis a partir do estado atual
    movimentos = []
    for i in range(8):
        for j in range(8):
            movimentos.append([
                [casa
                if mr.MaquinaRegras.geraMovimentosPossiveis(i, j, tabuleiro.estado, 1 if not jogadorMax else 2)[i][j]
                else tabuleiro.estado[i][j]
                for j, casa in enumerate(linha)]
                for i, linha in enumerate(tabuleiro.estado)]
            )
    return movimentos



def minimax(profundidade, tabuleiro, alpha, beta, ehJogadorMax):
    if profundidade == 0:
        return (None, -avaliaEstado(tabuleiro)) #ia começa pela peça preta

    movimentosPossiveis = pegaMovimentos(tabuleiro, ehJogadorMax)

    if ehJogadorMax:
        melhorPontuacao = -9999
        for movimento in movimentosPossiveis:
            #executa movimento
            tabuleiroAntes = tabuleiro.copiaInstancia()
            tabuleiro.estado = movimento
            pontuacaoJogada = avaliaEstado(tabuleiro)
            jogada, pontuacao = minimax(profundidade-1, tabuleiro, alpha, beta, not ehJogadorMax)
            if pontuacaoJogada > pontuacao:
                pontuacao = pontuacaoJogada
                jogada = movimento
            #jogada = tabuleiro.copiaInstancia()
            #desfaz jogada
            tabuleiro = tabuleiroAntes
            if pontuacao > melhorPontuacao:
                melhorPontuacao, melhorJogada = pontuacao, jogada
            alpha = max(alpha, melhorPontuacao)
            if beta <= alpha:
                # melhorJogada, melhorPontuacao = jogada, pontuacao
                return (melhorJogada, melhorPontuacao)
        return (melhorJogada, melhorPontuacao)
    else:
        melhorPontuacao = 9999
        for movimento in movimentosPossiveis:
            #executa movimento
            tabuleiroAntes = tabuleiro.copiaInstancia()
            tabuleiro.estado = movimento
            pontuacaoJogada = avaliaEstado(tabuleiro)
            jogada, pontuacao = minimax(profundidade-1, tabuleiro, alpha, beta, not ehJogadorMax)
            if pontuacaoJogada < pontuacao:
                pontuacao = pontuacaoJogada
                jogada = movimento
            #salvarJogada = tabuleiro.copiaInstancia().estado
            #desfaz jogada
            tabuleiro = tabuleiroAntes
            if pontuacao < melhorPontuacao:
                melhorPontuacao, melhorJogada = pontuacao, jogada
            beta = min(beta, melhorPontuacao)
            if beta <= alpha:
                #melhorJogada,melhorPontuacao = jogada, pontuacao
                return (melhorJogada, melhorPontuacao)
        return (melhorJogada, melhorPontuacao)

def joga(tabuleiro):
    jogadaDaIA, _ = minimax(3, tabuleiro, -10000, 10000, True)
    tabuleiro.estado = jogadaDaIA
    tabuleiro.avancaTurno()