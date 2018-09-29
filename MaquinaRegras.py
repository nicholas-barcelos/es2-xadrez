class MaquinaRegras:
    def __init__(self):
        pass

    @staticmethod
    def validaMovimentacao(xOrigem, yOrigem, xDestino, yDestino, estado):
        peca = estado[xOrigem][yOrigem]
        deslocVer = xOrigem - xDestino
        deslocHor = yOrigem - yDestino

        if(peca == "T"):
            if(deslocVer == 0 or deslocHor == 0):
                return True
        elif(peca == "B"):
            if(deslocHor < 0): deslocHor*=-1
            if (deslocVer < 0): deslocVer *= -1
            if(deslocHor == deslocVer): return True
        elif(peca == "K"):
            if(deslocHor < 0): deslocHor*=-1
            if(deslocVer < 0): deslocVer *= -1
            if(deslocHor < 2 and deslocVer < 2):
                return True
        elif(peca == "P"):
            print("dy = ", deslocVer)
            if(((deslocVer == 1) or (xOrigem == 6 and deslocVer == 2)) and deslocHor == 0): return True
        elif(peca == "H"):
            if(deslocHor < 0): deslocHor*=-1
            if (deslocVer < 0): deslocVer *= -1
            if((deslocHor == 2 and deslocVer == 1) or (deslocHor == 1 and deslocVer == 2)): return True
        elif(peca == "Q"):
            if(deslocHor < 0): deslocHor*=-1
            if(deslocVer < 0): deslocVer *= -1

            if(deslocVer == 0 or deslocHor == 0) : return True
            elif(deslocHor == deslocVer): return True

        return False

    def validaRoque(self):
        print("Roque")

    def validaEnPassant(self):
        print("EnPassant")

    def validaEmpate(self):
        print("Empate")

    def validaPromocao(self):
        print("Promove")

    def validaCaptura(self):
        print("Captura")

    def validaVitoria(self):
        print("Vitoria")

    def validaCheque(self):
        print("cheque")
