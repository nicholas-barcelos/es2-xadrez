class MaquinaRegras:
    def __init__(self):
        pass

    #Metodo que verifica se a movimentacao eh valida (soh se usa o maiusculo pq a ia ira inverter o tabuleiro para ficar mais pratico)
    @staticmethod
    def validaMovimentacao(xOrigem, yOrigem, xDestino, yDestino, estado, turno):
        peca = estado[xOrigem][yOrigem]
        deslocVer = xOrigem - xDestino
        deslocHor = yOrigem - yDestino

        if(turno == 2):
            peca = peca.upper()
            if(peca == "P"): deslocVer *= -1

        if(peca == "P"):
            if((deslocHor == 1 or deslocHor == -1)
                and estado[xDestino][yDestino] != " "
                and deslocVer == 1):
                return True
            if(deslocVer == 1 and deslocHor == 0 and estado[xDestino][yDestino] == " "): return True
            if((xOrigem == 6 or xOrigem == 1) and deslocVer == 2 and deslocHor == 0): return True
            return False

        if (deslocHor < 0): deslocHor *= -1
        if (deslocVer < 0): deslocVer *= -1

        #Movimento do REI e do Cavalo:
        if (peca == "K" or peca == 'k'):
            if (deslocHor < 2 and deslocVer < 2):
                return True
            return False
        if (peca == "H" or peca == 'h'):
            if ((deslocHor == 2 and deslocVer == 1) or (deslocHor == 1 and deslocVer == 2)):
                return True
            return False

        if(deslocHor == 0 and (peca == "Q" or peca == "T")):
            pecaColidida = MaquinaRegras.verificaColisaoVertical(xOrigem, xDestino, yOrigem, estado)
            return pecaColidida == " "
        elif(deslocVer == 0 and (peca == "Q" or peca == "T")):
            pecaColidida = MaquinaRegras.verificaColisaoHorizontal(yOrigem, yDestino, xOrigem, estado)
            return pecaColidida == " "
        elif(deslocHor == deslocVer and (peca == "Q" or peca == "B")):
            pecaColidida = MaquinaRegras.verificaColisaoDiagonal(xOrigem,yOrigem, xDestino, yDestino,estado)
            return pecaColidida == " "

        return False

    def validaRoque(self):
        print("Roque")

    @staticmethod
    def verificaColisaoVertical(xOrigem, xDestino, y, estado):
        i = min(xOrigem, xDestino) + 1
        while (i < max(xOrigem, xDestino)):
            if(estado[i][y] != " "): return estado[i][y]
            i+=1
        return " "

    @staticmethod
    def verificaColisaoHorizontal(yOrigem, yDestino, x, estado):
        i = min(yOrigem, yDestino) + 1
        while (i < max(yDestino, yOrigem)):
            if (estado[x][i] != " "): return estado[x][i]
            i += 1
        return " "

    @staticmethod
    def verificaColisaoDiagonal(xOrigem, yOrigem, xDestino, yDestino, estado):
        passoX = 1 if (xOrigem < xDestino) else -1
        passoY = 1 if (yOrigem < yDestino) else -1
        xOrigem = xOrigem + passoX
        yOrigem = yOrigem + passoY
        while (yOrigem != yDestino):
            if (estado[xOrigem][yOrigem] != " "):
                return estado[xOrigem][yOrigem]
            xOrigem = xOrigem + passoX
            yOrigem = yOrigem + passoY
        return " "

    @staticmethod
    def verificaCheque(rei, estado):
        return True


    def validaEnPassant(xOrigem,yOrigem,xDestino,yDestino,peaoEnPassant, estado):
        #so entra caso seja um peão
        if(estado[xOrigem][yOrigem].lower =='p'):
            #caso o enPassant nâo tenha acontecido, ou não seja do turno passado ou seja de uma peça da mesma cor
            if peaoEnPassant == [0,0,0] or peaoEnPassant[2]!= estado.contadorTurno-1 or estado[peaoEnPassant[0],peaoEnPassant[1]] == estado[xOrigem,yOrigem]:
                return False
            peca = estado[xOrigem][yOrigem]
            deslocVer = xOrigem - xDestino
            deslocHor = yOrigem - yDestino

            if((deslocHor == 1 and deslocVer == 1) and peaoEnPassant[0]==xOrigem-1 and peaoEnPassant[1]==yOrigem):
                #caso pB branco come
                return True
            elif((deslocHor == -1 and deslocVer == -1)and peaoEnPassant[0]==xOrigem+1 and peaoEnPassant[1]==yOrigem):
                #caso pB preto come
                return True
            elif((deslocHor == 1 and deslocVer == -1)and peaoEnPassant[0]==xOrigem+1 and peaoEnPassant[1]==yOrigem):
                #caso Bp preto come
                return True
            elif((deslocHor == -1 and deslocVer == 1)and peaoEnPassant[0]==xOrigem+1 and peaoEnPassant[1]==yOrigem):
                #caso Bp branco come
                return True
            else:
                return False

        if yOrigem == peaoEnPassant[1]+1 or yOrigem == peaoEnPassant[1]-1: return True
        return False

    def validaEmpate(self):
        print("Empate")

    @staticmethod
    def validaPromocao(estado, xPeca, yPeca):
        print("chamou promocao %s %d %d" % (estado[xPeca][yPeca], xPeca, yPeca))
        if estado[xPeca][yPeca] == "p" and xPeca == 7:
            print("promove")
            escolha = "q"
            estado[xPeca][yPeca] = escolha.lower()
            return True
        if estado[xPeca][yPeca] == "P" and xPeca == 0:
            print("PROMOVE")
            escolha = "q"
            estado[xPeca][yPeca] = escolha.upper()
            return True
        return False

    def validaCaptura(self):
        print("Captura")

    def validaVitoria(self):
        print("Vitoria")

    def validaCheque(self):
        print("cheque")

    @staticmethod
    def geraMovimentosPossiveis(xOrigem, yOrigem, estado, turno):
        movimentos = [[ MaquinaRegras.validaMovimentacao(xOrigem, yOrigem, i, j, estado, turno) for j, _ in enumerate(row) ] for i, row in enumerate(estado)]
        return movimentos