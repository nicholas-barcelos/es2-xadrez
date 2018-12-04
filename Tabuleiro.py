import copy
import MaquinaRegras as mr
import Cemiterio as grv
import AI_bkp as ai
class Tabuleiro:
    instancia = None
    estado = [
        ["t", "h", "b", "k", "q", "b", "h", "t"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["T", "H", "B", "Q", "K", "B", "H", "T"]
    ]
    pecaSelecionada = " "
    xSelecionado = 1
    ySelecionado = 1
    dimensao = 400
    casa = dimensao // 8
    offsetX = 16
    offsetY = 40
    #Posicao do Rei para verificar o cheque
    rei = [7,4]
    rei2= [0,3]
    peaoEnPassant = [0,0,0]#recebendo [x,y,turno]
    jogador = None
    contadorTurno = 0
    cemiterio = None

    def __init__(self):
        self.cemiterio = grv.Cemiterio.pegaInstancia()

    @staticmethod
    def pegaInstancia():
        if not Tabuleiro.instancia:
            Tabuleiro.instancia = Tabuleiro()
        return Tabuleiro.instancia

    @staticmethod
    def copiaInstancia():
        if not Tabuleiro.instancia:
            raise Exception('No instance error')
        return copy.deepcopy(Tabuleiro.instancia)


    def destroi(self):
        print("Destruir")

    def inverte(self):
        print("Inverte")

    def avancaTurno(self):
        self.contadorTurno += 1
        if self.pegaJogadorAtual() == 2:
           ai.joga(self.pegaInstancia())

    def pegaJogadorAtual(self):
        return (self.contadorTurno % 2) + 1

    def pegaPecaSelecionada(self):
        return self.pecaSelecionada

    def manipulaClique(self, x, y):
        pecaClicada = self.estado[x][y]
        print('x: ', x, " y: ", y)
        if(pecaClicada.isupper() and self.pegaJogadorAtual()==1
            or pecaClicada.islower() and self.pegaJogadorAtual()==2):
            self.pecaSelecionada = pecaClicada
            # movimentosPossiveis = mr.MaquinaRegras.geraMovimentosPossiveis(x, y, self.estado, self.pegaJogadorAtual())
            # for i in movimentosPossiveis:
            #     for j in i:
            #         print(j, end=' ')
            #     print()
            self.xSelecionado = x
            self.ySelecionado = y
            return False
        elif(self.pecaSelecionada != " "):
            tentativa = self.movePeca(x, y)
            if(tentativa and pecaClicada != " "):
                self.cemiterio.adicionaPeca(pecaClicada, self)
            return tentativa
        return False

    def removePeca(self, x, y):
        self.estado[x][y] = " "

    def trocarPeca(self, x, y):
        print("Trocar posicao")

    def retornaPeca(self, x, y):
        print("Nao lembro")

    def movePeca(self, xDestino, yDestino):
        if (mr.MaquinaRegras.validaMovimentacao(self.xSelecionado, self.ySelecionado, xDestino, yDestino, self.estado, self.pegaJogadorAtual())):
            self.estado[xDestino][yDestino] = self.estado[self.xSelecionado][self.ySelecionado]
            if(not mr.MaquinaRegras.verificaCheque(self.rei, self.estado)):
                self.estado[xDestino][yDestino] = " "
                print("Rei em Cheque")
                return False
            self.estado[self.xSelecionado][self.ySelecionado] = " "
            self.pecaSelecionada = " "
            print("Pode Movimentar")
            mr.MaquinaRegras.validaPromocao(self.estado, xDestino, yDestino)
            self.avancaTurno()
            return True
        elif (mr.MaquinaRegras.validaEnPassant(self.xSelecionado,self.ySelecionado,xDestino,yDestino,self.peaoEnPassant,self.estado)):
            self.estado[xDestino][yDestino] = self.estado[self.xSelecionado][self.ySelecionado]
            if(not mr.MaquinaRegras.verificaCheque(self.rei, self.estado)):
                self.estado[xDestino][yDestino] = " "
                print("Rei em Cheque")
                return False
            self.estado[self.xSelecionado][self.ySelecionado] = ' '
            self.cemiterio.adicionaPeca(self.peaoEnPassant[2], self)
            self.estado[self.peaoEnPassant[0]][self.peaoEnPassant[1]] = ' '
            self.avancaTurno()
            return True
        print("Não pode Movimentar")
        return False

    def inverte(self):
        tam = self.estado.__len__()
        for x in range(int(tam/2)):
            for y in range(tam):
                peca = self.estado[x][y]
                xInverso = tam - x - 1
                yInverso = tam - y - 1
                aux = self.estado[xInverso][yInverso]
                self.estado[xInverso][yInverso] = peca
                self.estado[x][y] = aux