class No():
    def __init__(self,dado):
        self.dado = dado
        self.prox = None
    def getDado(self):
        return self.dado
    def getProx(self):
        return self.prox
    def setProx(self,novoNo):
        self.prox = novoNo

class Fila():
    def __init__(self):
        self._inicio = None
        self._fim =  None

    def insertAtEnd(self,dado):
        novoNo = No(dado)
        if self._inicio != None:
            self._fim.setProx(novoNo)
            self._fim =  novoNo
        else:
            self._inicio = novoNo
            self._fim = novoNo
            

    def remover(self):
        valorPrimeiroNo = self._inicio.getDado()
        if self._inicio == self._fim:
            self._inicio = None
            self._fim = None
        else:
            self._inicio = self._inicio.getProx()
        return valorPrimeiroNo

    def firstelem(self):
        return self._inicio.getDado()
    def reset(self):
        self._inicio = self._fim = None
        
    def _str_(self):
        s = ''
        b = self.getInicio()
        cont = 1
        while b is not None:
            if cont == 1:
                s += str(b.getData())
                b = b.getnex()
                cont = 0
            else:
                s += ' '+ str(b.getData())
                b = b.getnex()
        return s
    
    

deck_mesa = Fila()
qntFestas= int(input())
jogadores = {}
for festas in range(qntFestas):
    chave = 1;cont = 1;achou = False
    deck = input().split()
    for x in deck:
        deck_mesa.insertAtEnd(int(x))
    while True:
        deck_convidados = input().split()
        conv = [int(c) for c in deck_convidados]
        if conv[0] == -1:
            break
        jogadores[chave] = conv
        chave+=1
    while True:
        if cont > 1000:
            print("0")
            break
        elif achou is True:
            break
        topDeck = deck_mesa.firstelem()
        for num in range(len(jogadores)):
            cartas = jogadores[num+1]
            if len(cartas) == 0:
                achou = True
                print(num+1)
                break
            if len(cartas) > 0:
                top = cartas[0]
                if top == topDeck:
                    cartas.remove(top)
                else:
                    cartas.append(top)
                    cartas.remove(top)
        deck_mesa.remover()
        deck_mesa.insertAtEnd(topDeck)
        cont+=1
    jogadores.clear()
    deck_mesa.reset()


