import Heuristica as hr
import MaquinaRegras as mr
import copy

def ehMesmoCase(a, b):
    return (a.isupper() and b.isupper()) or (a.islower() and b.islower())

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
            peca = tabuleiro.estado[i][j]
            atualMovimentosPossiveis = mr.MaquinaRegras.geraMovimentosPossiveis(i, j, tabuleiro.estado, 2 if jogadorMax else 1)
            posicoesParaPeca = [(i, j) for i, linha in enumerate(atualMovimentosPossiveis) for j, casa in enumerate(linha) if casa and not ehMesmoCase(tabuleiro.estado[i][j], peca)]
            if not posicoesParaPeca:
                continue
            while posicoesParaPeca:
                l,c = posicoesParaPeca[0]
                posicoesParaPeca = posicoesParaPeca[1:]
                movimentosParaPeca = copy.deepcopy(tabuleiro.estado)
                movimentosParaPeca[i][j] = " "
                movimentosParaPeca[l][c] = peca
                movimentos.append(movimentosParaPeca)
    return movimentos

def raizMinimax(profundidade, tabuleiro, ehJogadorMax):
    movimentosPossiveis = pegaMovimentos(tabuleiro, True)
    melhorPontuacao = -9999.0
    melhorMovimentoEncontrado = []

    for movimento in movimentosPossiveis:
        tabuleiroAntes = tabuleiro.copiaInstancia()
        tabuleiro.estado = movimento
        pontuacao = minimax(profundidade-1, tabuleiro, -10000.0, 10000.0, not ehJogadorMax)
        tabuleiro = tabuleiroAntes
        if pontuacao >= melhorPontuacao:
            melhorPontuacao = pontuacao
            melhorMovimentoEncontrado = movimento
    return melhorMovimentoEncontrado

def minimax(profundidade, tabuleiro, alpha, beta, ehJogadorMax):
    if profundidade == 0:
        return -avaliaEstado(tabuleiro)

    movimentosPossiveis = pegaMovimentos(tabuleiro, ehJogadorMax)

    if ehJogadorMax:
        melhorPontuacao = -9999.0;
        for movimento in movimentosPossiveis:
            tabuleiroAntes = tabuleiro.copiaInstancia()
            tabuleiro.estado = movimento
            melhorPontuacao = max(melhorPontuacao, minimax(profundidade - 1, tabuleiro, alpha, beta, not ehJogadorMax))
            tabuleiro = tabuleiroAntes
            alpha = max(alpha, melhorPontuacao)
            if beta <= alpha:
                return melhorPontuacao
        return melhorPontuacao
    else:
        melhorPontuacao = 9999.0
        for movimento in movimentosPossiveis:
            tabuleiroAntes = tabuleiro.copiaInstancia()
            tabuleiro.estado = movimento
            melhorPontuacao = min(melhorPontuacao, minimax(profundidade - 1, tabuleiro, alpha, beta, not ehJogadorMax))
            tabuleiro = tabuleiroAntes
            beta = min(beta, melhorPontuacao)
            if beta <= alpha:
                return melhorPontuacao
        return melhorPontuacao

def pegaMelhorMovimento(profundidade, tabuleiro):
    # if (game.game_over()):
    #    print("game over")
    melhorMovimento = raizMinimax(profundidade, tabuleiro, True)
    return melhorMovimento

def joga(tabuleiro):
    pecasBrancasAntes = ["%s %d %d" % (peca, i, j) for i, linha in enumerate(tabuleiro.estado) for j,peca in enumerate(linha) if peca.isupper()]
    jogadaDaIA = pegaMelhorMovimento(3, tabuleiro.copiaInstancia())
    pecasBrancasDepois = ["%s %d %d" % (peca, i, j) for i, linha in enumerate(jogadaDaIA) for j,peca in enumerate(linha) if peca.isupper()]
    tabuleiro.estado = jogadaDaIA
    pecaMorta = [peca[0] for peca in pecasBrancasAntes if peca not in pecasBrancasDepois]
    if pecaMorta:
        tabuleiro.cemiterio.adicionaPeca(pecaMorta[0], tabuleiro)
    tabuleiro.avancaTurno()
