import Heuristica as hr
import MaquinaRegras as mr
class AI:
    def __init__(self):
        pass

    @staticmethod
    def avaliaEstado(tabuleiro):
        valorTabuleiro = 0
        for i in range(8):
            for j in range(8):
                valorTabuleiro += hr.Heuristica.pegaValorPeca(tabuleiro.estado[i][j], i, j)
        return valorTabuleiro

    @staticmethod
    def pegaMovimentos(tabuleiro):
        #vai pegar proximos estados possiveis a partir do estado atual
        movimentos = []
        for i in range(8):
            for j in range(8):
                movimentosPeca = mr.MaquinaRegras.geraMovimentosPossiveis(i,j,tabuleiro.estado, tabuleiro.pegaJogadorAtual())
                movimentos.append(
                    [ casa if not movimentosPeca[i][j] else tabuleiro.estado[i][j] for casa in [linha for linha in tabuleiro.estado] ]
                )
                #movimentos.append(
                #    map(lambda linha: map(lambda casa: tabuleiro.estado[i][j] if movimentosPeca[i][j] else casa, linha)
                #        , tabuleiro.estado))
        return movimentos


    @staticmethod
    def minimax(profundidade, tabuleiro, alpha, beta, ehJogadorMax):
        if profundidade == 0:
            return (None, -avaliaEstado(tabuleiro)) #ia começa pela peça preta

        movimentosPossiveis = AI.pegaMovimentos(tabuleiro)

        if ehJogadorMax:
            melhorPontuacao = -9999
            for movimento in movimentosPossiveis:
                #executa movimento
                tabuleiroAntes = tabuleiro.copiaInstancia()
                tabuleiro.estado = movimento
                pontuacao = AI.avaliaEstado(tabuleiro)
                jogada, pontuacao = max(pontuacao, minimax(profundidade-1, tabuleiro, alpha, beta, not ehJogadorMax))
                jogada = tabuleiro.copiaInstancia()
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
                pontuacao = AI.avaliaEstado(tabuleiro)
                jogada, pontuacao = max(pontuacao, minimax(profundidade-1, tabuleiro, alpha, beta, not ehJogadorMax))
                jogada = tabuleiro.copiaInstancia()
                #desfaz jogada
                tabuleiro = tabuleiroAntes
                if pontuacao < melhorPontuacao:
                    melhorPontuacao, melhorJogada = pontuacao, jogada
                beta = min(beta, melhorPontuacao)
                if beta <= alpha:
                    #melhorJogada,melhorPontuacao = jogada, pontuacao
                    return (melhorJogada, melhorPontuacao)
            return (melhorJogada, melhorPontuacao)

    @staticmethod
    def joga(tabuleiro):
        jogadaDaIA, _ = AI.minimax(3, tabuleiro, -10000, 10000, True)
        tabuleiro.estado = jogadaDaIA
        tabuleiro.avancaTurno()