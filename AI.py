import Heuristica
import MaquinaRegras as mr
class AI:
    def __init__(self):
        pass

    @staticmethod
    def avaliaEstado(tabuleiro):
        valorTabuleiro = 0
        for i in range(8):
            for j in range(8):
                valorTabuleiro += Heuristica.pegaValorPeca(tabuleiro[i][j], i, j)
        return valorTabuleiro

    @staticmethod
    def pegaMovimentos(tabuleiro):
        #vai pegar proximos estados possiveis a partir do estado atual
        pass


    @staticmethod
    def minimax(profundidade, tabuleiro, alpha, beta, ehJogadorMax):
        if depth == 0:
            return (None, -avaliarEstado(tabuleiro)) #ia começa pela peça preta

        movimentosPossiveis = pegaMovimentos(tabuleiro)

        if ehJogadorMax:
            melhorPontuacao = -9999
            for movimento in movimentosPossiveis:
                #executa movimento
                melhorJogada, melhorPontuacao = max(melhorPontuacao, minimax(profundidade-1, tabuleiro, alpha, beta, !ehJogadorMax))
                jogada = tabuleiro.copiaInstancia()
                #desfaz jogada
                alpha = max(alpha, melhorPontuacao)
                if(beta <= alpha)
                    melhorJogada = jogada
                    return (melhorJogada, melhorPontuacao)
            melhorJogada = jogada
            return (melhorJogada, melhorPontuacao)
        else:
            melhorMovimento = 9999
            for movimento in movimentosPossiveis:
                #executa movimento
                melhorJogada, melhorPontuacao = max(melhorPontuacao, minimax(profundidade-1, tabuleiro, alpha, beta, !ehJogadorMax))
                jogada = tabuleiro.copiaInstancia()
                #desfaz jogada
                beta = min(beta, melhorPontuacao)
                if(beta <= alpha)
                    melhorJogada = jogada
                    return (melhorJogada, melhorPontuacao)
            melhorJogada = jogada
            return (melhorJogada, melhorPontuacao)