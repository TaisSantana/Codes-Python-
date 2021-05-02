'''
Ninguém aguenta mais filas

Com a proximidade da Copa do Mundo, o fluxo de pessoas nas filas para compra de ingressos
aumentou consideravelmente. Como as filas estão cada vez maiores, pessoas menos pacientes
tendem a desistir da compra de ingressos e acabam deixando as filas, liberando assim vaga para
outras pessoas. Quando uma pessoa deixa a fila, todas as pessoas que estavam atrás dela dão um
passo a frente, sendo assim nunca existe um espaço vago entre duas pessoas. A fila inicialmente
contém N pessoas, cada uma com um identificador diferente. Juvenal sabe o estado inicial dela e os
identificadores em ordem das pessoas que deixaram a fila. Sabendo que após o estado inicial
nenhuma pessoa entrou mais na fila, Juvenal deseja saber o estado final da fila.

Entrada
A primeira linha contém um inteiro N representando a quantidade de pessoas inicialmente na fila. A
segunda linha contém N inteiros representando os identificadores das pessoas na fila. O primeiro
identificador corresponde ao identificador da primeira pessoa na fila. É garantido que duas pessoas
diferentes não possuem o mesmo identificador. A terceira linha contém um inteiro M representando
a quantidade de pessoas que deixaram a fila. A quarta linha contém M inteiros representando os
identificadores das pessoas que deixaram a fila, na ordem em que elas saíram. É garantido que um
mesmo identificador não aparece duas vezes nessa lista.

Saída
Seu programa deve imprimir uma linha contendo N-M inteiros com os identificadores das pessoas
que permaneceram na fila, em ordem de chegada. 
-----------------------------------------------------------------------------------------------------

Resolução:
'''
class Node:
    def __init__(self,data, nex=None, prev=None):
        self.data = data
        self.nex = nex
        self.prev = prev
    def getData(self):
        return self.data
    def setData(self, dado):
        self.data = dado

    def getnex(self):
        return self.nex
    def setnex(self, nex):
        self.nex = nex

    def getprev(self):
        return self.prev
    def setprev(self, prev):
        self.prev = prev
        
class LDE:
    def __init__(self, inicio=None, fim=None):
        self._inicio = inicio
        self.fim = fim

    def getInicio(self):
        return self.inicio
    def setInicio(self, inicio):
        self.inicio = inicio
    def getEnd(self):
        return self.fim
    def setEnd(self, fim):
        self.fim = fim

    def isEmpty(self):
        return self.getInicio() == None

        
    def insertAtEnd(self, val):
        ie = Node(val)
        if self.getEnd() != None: #se dif lista vazia
            self.getEnd().setnex(ie)
            ie.setprev(self.getEnd()) #i aponta p 'e'
            self.setEnd(ie) #substitui fim por i
            
            
        else: #inicio e fim sao i.
            self.setInicio(ie)
            self.setEnd(ie)
            ie.setnex(None)
            ie.setprev(None)
     
        
    def remover(self,val):
            a = self.getInicio()
            while a is not None:
                if a.getData() == val:
                    if a.getprev() == a.getnex() == None: #so um elem
                        self.setInicio(None)
                        self.setEnd(None)
                    if a.getprev() == None: #a é prim elem da lista, +de 1 elem
                        a.getnex().setprev(None)
                        self.setInicio(a.getnex())
                    elif a.getnex() == None: #se ultmo elem lista, + de 1 elem
                        a.getprev().setnex(None)
                        self.setEnd(a.getprev())
                    else:
                        a.getnex().setprev(a.getprev())
                        a.getprev().setnex(a.getnex())
                a = a.getnex()
            

    def __str__(self):
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

n = int(input()) #qndd inic de pessoas na fila
listaprov = map(int,input().split()) 
lista = LDE()
for elem in listaprov:
    lista.insertAtEnd(elem)

d = int(input()) #qntdd pessoas q deixaram fila.
deixaram = map(int,input().split())
for elem in deixaram:
    lista.remover(elem)
print(lista)
    
