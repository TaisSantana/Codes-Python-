'''Calculadora improvisada
O Tio de Juvenal, Roberval, quer financiar um carro. Juvenal está dizendo para ele que
financiamentos colocam a corda no pescoço de todos e que ele deveria economizar para comprar o
carro à vista. Então, como Roberval é uma pessoa pragmática, ele pediu para seu sobrinho mostrar
os cálculos de quanto ele vai ter que pagar, de fato, pelo futuro carro. No entanto, Juvenal está com
um problema: ele não tem calculadora e seu computador está com o processador quebrado. Mais
especificamente, a Unidade Lógico Aritmética (ULA) do processador está executando apenas a
operação “+1”, também conhecida como sucessor. Juvenal está desesperado, pois precisa realizar
operações mais elaboradas para calcular os juros e não permitir que seu tio faça uma grande besteira
financiando aquele carro. Juvenal então decidiu pedir sua ajudar para elaborar um programa de
computador que realize as operações de sucessor, soma, multiplicação e exponenciação que seja
executado em seu computador defeituoso.

Tarefa
Implemente um programa que implemente as operações de soma, multiplicação e exponenciação
usando apenas a operação de sucessor.

Entrada

A entrada deverá ser lida do teclado e consiste de várias operações. Cada linha representa uma
operação. Cada operação pode ser escrita em uma das seguintes maneiras.
Sucessor, onde A é um número inteiro >= 0:
Suc A
Soma, onde A, B são números inteiros >= 0:
Soma A B
Multiplicação, onde A, B são números inteiros >= 0
Mult A B
Exponenciação, onde A, B são números inteiros >= 0
Exp A B

Saída

Escreva em cada linha da saída o resultado da operação correspondente.
Resolução:
'''
def Suc(x):
    return x+1

def Soma(x,y):
    c = x
    for i in range(y):
        c = Suc(c)
    return c

def Mult(x,y):
    c = 0
    for i in range(y):
        c = Soma(c,x)
    return c

def Exp(x,y):
    c = x
    for i in range(y-1):
        c = Mult(c,x)
    return c
    
#------------------------------
while True:
    try:
        entrada = input().split()
        if entrada[0]== "Suc":
            res = Suc(int(entrada[1]))
            print(res)
            
        elif entrada[0]== "Soma":
            res = Soma(int(entrada[1]),int(entrada[2]))
            print(res)
            
        elif entrada[0]== "Mult":
            res = Mult(int(entrada[1]),int(entrada[2]))
            print(res)
            
        elif entrada[0]== "Exp":
            res = Exp(int(entrada[1]),int(entrada[2]))
            print(res)

    except:
        break
    
