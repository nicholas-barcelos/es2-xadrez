
import MaquinaRegras as mr
import Cemiterio as grv
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
    xSelecionado = None
    ySelecionado = None
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
        return Tabuleiro.instancia.copy()


    def destroi(self):
        print("Destruir")

    def inverte(self):
        print("Inverte")

    def avancaTurno(self):
        self.contadorTurno += 1

    def pegaJogadorAtual(self):
        return (self.contadorTurno % 2) + 1

    def manipulaClique(self, x, y):
        pecaClicada = self.estado[x][y]
        print('x: ', x, " y: ", y)
        if(pecaClicada.isupper() and self.pegaJogadorAtual()==1 or pecaClicada.islower() and self.pegaJogadorAtual()==2):
            self.pecaSelecionada = pecaClicada
            self.xSelecionado = x
            self.ySelecionado = y
            return False
        elif(self.pecaSelecionada != " "):
            tentativa = self.movePeca(x, y)
            if(tentativa is False and self.estado[x][y].lower == 'p'):
                tentativa = self.enPassant(x,y)
            if(tentativa and pecaClicada.islower()):
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
        if (mr.MaquinaRegras.validaMovimentacao(self.xSelecionado, self.ySelecionado, xDestino, yDestino, self.estado)):
            self.estado[xDestino][yDestino] = self.estado[self.xSelecionado][self.ySelecionado]
            if(not mr.MaquinaRegras.verificaCheque(self.rei, self.estado)):
                self.estado[xDestino][yDestino] = " "
                print("Rei em Cheque")
                return False
            self.estado[self.xSelecionado][self.ySelecionado] = " "
            self.pecaSelecionada = " "
            print("Pode Movimentar")
            self.avancaTurno()
            return True
        print("Não pode Movimentar")
        return False

    def enPassant(self,xDestino,yDestino):
        if mr.MaquinaRegras.validaEnPassant(self.xSelecionado,self.ySelecionado,self.peaoEnPassant,self.estado):
            if(not mr.MaquinaRegras.verificaCheque(self.rei, self.estado)):
                self.estado[xDestino][yDestino] = " "
                print("Rei em Cheque")
                return False
            self.estado[xDestino][yDestino] = self.estado[self.xSelecionado][self.ySelecionado]
            self.estado[self.xSelecionado][self.ySelecionado] = " "
            self.estado[self.peaoEnPassant[0]][self.peaoEnPassant[1]] = " "
            self.peaoEnPassant = [0,0,0]
            return True
        return False



