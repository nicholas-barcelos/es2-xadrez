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


    def verificaChequeMate(self,rei, estado,turno,chequeReis):
        if rei== "K" and chequeReis[1]:
            if(self.geraMovimentosPossiveis(rei[0],rei[1],estado,turno) is [ ]): return True
        if rei == "k" and chequeReis[0]:
            if (self.geraMovimentosPossiveis(rei[0], rei[1], estado, turno) is []): return True
        return False

    def verificaEmpate(self,numeroMovimentos,rei,estado, turno):
        if(numeroMovimentos>=50):return True
        if(turno>30 and self.geraMovimentosPossiveis(rei[0],rei[1],estado,turno)==[]): return True
        return False


    def validaRoque(self,xOrigem,yOrigem,xDestino,yDestino,estado):
        rei = estado[xOrigem][yOrigem]
        if(estado[xOrigem][yOrigem].upper()=='K'):
            if(xOrigem==7 and yOrigem==4):
                if(estado[xDestino][yDestino].upper()=='T'):
                    if(xDestino==7 and yDestino==7):
                        if(self.verificaColisaoHorizontal(yOrigem, yDestino, xOrigem, estado)==estado[xDestino][yDestino]):
                            if self.validaCheque(estado, xOrigem, yOrigem +1,rei) \
                                    or self.validaCheque(estado, xOrigem, yOrigem +2,rei):
                                return False
                            else:
                                return True
                    elif(xDestino==7 and yDestino==0):
                        if(self.verificaColisaoHorizontal(yOrigem, yDestino, xOrigem, estado)==estado[xDestino][yDestino]):
                            if(self.validaCheque(estado,xOrigem,yOrigem-1,rei)or self.validaCheque(estado,xOrigem,yOrigem-2,rei)):
                                return False
                            else:
                                return True

            elif (xOrigem==0 and yOrigem==3):
                if(estado[xDestino][yDestino].upper()=='T'):
                    if(xDestino==0 and yDestino==7):
                        if(self.verificaColisaoHorizontal(yOrigem, yDestino, xOrigem, estado)==estado[xDestino][yDestino]):
                            if(self.validaCheque(estado,xOrigem,yOrigem+1,rei)or self.validaCheque(estado,xOrigem,yOrigem+2,rei)):
                                return False
                            else:
                                return True
                    elif(xDestino==0 and yDestino==0):
                        if(self.verificaColisaoHorizontal(yOrigem, yDestino-1, xOrigem, estado)==estado[xDestino][yDestino]):
                            if(self.validaCheque(estado,xOrigem,yOrigem-1,rei)or self.validaCheque(estado,xOrigem,yOrigem-2,rei)):
                                return False
                            else:
                                return True

        return False

    def validaEnPassant(self,xOrigem,yOrigem,xDestino,yDestino,peaoEnPassant, estado):
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
    def validaPromocao(self,estado, xPeca, yPeca):
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

    def validaRange(self,numero):
        if(numero>-1) and (numero<8):
            return True
        else: return False


    def validaAliado(self,peca1,peca2):
        #Verifica se peças são iguais
        if(peca1.islower() and peca2.islower())or(peca1.isupper() and peca2.isupper()):
            return True
        return False

    def validaChequeCavalos(self,estado,xRei,yRei):
        rei = estado[xRei][yRei]
        if self.validaRange(xRei+1):
            if self.validaRange(yRei+2):
                peca = estado[xRei+1][yRei+2]
                if (not self.validaAliado(rei,peca)) and (peca.lower()=='h'):
                    return True
            if self.validaRange(yRei - 2):
                peca = estado[xRei + 1][yRei - 2]
                if (not self.validaAliado(rei, peca)) and (peca.lower() == 'h'):
                    return True

        if self.validaRange(xRei+2):
            if self.validaRange(yRei+1):
                peca = estado[xRei+2][yRei+1]
                if (not self.validaAliado(rei,peca)) and (peca.lower()=='h'):
                    return True
            if self.validaRange(yRei - 1):
                peca = estado[xRei + 2][yRei - 1]
                if (not self.validaAliado(rei, peca)) and (peca.lower() == 'h'):
                    return True

        if self.validaRange(xRei - 1):
            if self.validaRange(yRei + 2):
                peca = estado[xRei - 1][yRei + 2]
                if (not self.validaAliado(rei, peca)) and (peca.lower() == 'h'):
                    return True
            if self.validaRange(yRei - 2):
                peca = estado[xRei - 1][yRei - 2]
                if (not self.validaAliado(rei, peca)) and (peca.lower() == 'h'):
                    return True

        if self.validaRange(xRei - 2):
            if self.validaRange(yRei + 1):
                peca = estado[xRei - 2][yRei + 1]
                if (not self.validaAliado(rei, peca)) and (peca.lower() == 'h'):
                    return True
            if self.validaRange(yRei - 1):
                peca = estado[xRei - 2][yRei - 1]
                if (not self.validaAliado(rei, peca)) and (peca.lower() == 'h'):
                    return True
        return False


    def validaCheque(self,estado,xRei,yRei,rei):
        #Retorna True caso cheque, podemos mudar para retornar par posiçao para mostrar na tela
        print("cheque")
        #rei = estado[xRei][yRei]
        #verifica peoes
        if self.validaRange(xRei + 1) and self.validaRange(yRei + 1):
            peca = estado[xRei +1][yRei+1]
            if (not self.validaAliado(rei,peca)) and (peca.lower() == 'p' or peca.lower() =='q' or peca.lower()=='b'):
                return True
        if self.validaRange(xRei -1) and self.validaRange(yRei + 1):
            peca = estado[xRei -1][yRei+1]
            if (not self.validaAliado(rei,peca)) and (peca.lower() == 'p' or peca.lower() =='q' or peca.lower()=='b'):
                return True

        #verifica outras peças
        #Horizontal Direita:
        peca = self.verificaColisaoHorizontal(yRei, 7, xRei, estado)
        if (peca is not " ") and (not self.validaAliado(rei,peca)):
            if(peca.lower=='q' or peca.lower=='t'):
                return True

        #Horizontal esquerda:
        peca = self.verificaColisaoHorizontal(yRei, 0, xRei, estado)
        if (peca is not " ") and (not self.validaAliado(rei, peca)):
            if (peca.lower == 'q' or peca.lower == 't'):
                return True

        #Vertical cima:
        peca = self.verificaColisaoVertical(xRei, 7, yRei, estado)
        if (peca is not " ") and (not self.validaAliado(rei, peca)):
            if (peca.lower == 'q' or peca.lower == 't'):
                return True

        #Vertical baixo:
        peca = self.verificaColisaoVertical(xRei, 0, yRei, estado)
        if (peca is not " ") and (not self.validaAliado(rei, peca)):
            if (peca.lower == 'q' or peca.lower == 't'):
                return True

        #Diagonais Superiores
        #direita
        range = (7-yRei)
        peca = self.verificaColisaoDiagonal(xRei, yRei, xRei+range, yRei+range, estado)
        if (peca is not " ") and (not self.validaAliado(rei, peca)):
            if (peca.lower == 'q' or peca.lower == 'b'):
                return True
        #Esquerda
        range = max(xRei,yRei)
        peca = self.verificaColisaoDiagonal(xRei, yRei, xRei + range, yRei - range, estado)
        if (peca is not " ") and (not self.validaAliado(rei, peca)):
            if (peca.lower == 'q' or peca.lower == 'b'):
                return True

        # Diagonais Inferiores
        #Direita
        range = max(xRei-7, yRei-7)
        #ta indo de cima pra baixo e não ao contrario
        print("range: ",range," xrei: ",xRei," yRei",yRei)
        print(xRei-range)
        print(yRei+range)
        if xRei<8 and self.validaRange(yRei - range):
            peca = self.verificaColisaoDiagonal(xRei, yRei, xRei - range, yRei + range, estado)
            if (peca is not " ") and (not self.validaAliado(rei, peca)):
                if (peca.lower == 'q' or peca.lower == 'b'):
                    return True

        #Esquerda
        range = min(xRei, yRei)
        if xRei>0 and self.validaRange(yRei-range):
            peca = self.verificaColisaoDiagonal(xRei, yRei, xRei - range, yRei - range, estado)
            if (peca is not " ") and (not self.validaAliado(rei, peca)):
                if (peca.lower == 'q' or peca.lower == 'b'):
                    return True

        # verifica Cavalos
        if (self.validaChequeCavalos(estado,xRei,yRei)): return True

        return False

    @staticmethod
    def geraMovimentosPossiveis(xOrigem, yOrigem, estado, turno):
        movimentos = [[ MaquinaRegras.validaMovimentacao(xOrigem, yOrigem, i, j, estado, turno) for j, _ in enumerate(row) ] for i, row in enumerate(estado)]
        return movimentos
