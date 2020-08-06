'''
Quadrado 

Um quadrado quase mágico, de dimensões N N, é um quadrado que obedece à seguinte condição. Existe um número inteiro positivo M tal que: para qualquer linha, a soma dos números da linha é igual a M; e para qualquer coluna, a soma dos números da coluna é também igual a M. O quadrado seria mágico, e não apenas quase mágico, se a soma das
diagonais também fosse M. Por exemplo, a figura abaixo, parte (a), apresenta um quadrado quase mágico onde M = 21.
Laura construiu um quadrado quase mágico e alterou, propositalmente, um dos números!
Nesta tarefa, você deve escrever um programa que, dado o quadrado quase mágico alterado por Laura, descubra qual era o número original antes da alteração e qual número foi colocado no lugar. Por exemplo, na parte (b) da figura, o número original era 1, que Laura alterou para 7.

Entrada
A primeira linha da entrada contém apenas um número N, representando a dimensão do quadrado. As N linhas seguintes contêm, cada uma, N números inteiros, definindo o quadrado. A entrada é garantidamente um quadrado quase mágico onde exatamente um número foi alterado.

Saída
Seu programa deve imprimir apenas uma linha contendo dois números: primeiro o número
original e depois o número que Laura colocou no seu lugar.

Restrições
• 3<=N<=50; e o valor de todos os números está entre 1 e 10000
'''


lado = int(input()) #qntdd lados
square = [list(map(int,input().split())) for x in range(lado)] #formando linhas da matriz que forma o quadrado.
listasomas = []#lista p guardar somas e desc a soma True. 

for e in square:
    listasomas.append(sum(e))


b = 0 #indica a linha p coordenada errada do final
somaT = 0;somaF = 0
for elem in listasomas: #cada soma corresponde ao msm num da linha 
    if listasomas.count(elem) == 1 :
        somaF = elem #soma equivocada
        linha = b
    elif listasomas.count(elem) != 1 : 
        somaT = elem #valor correto da soma do sqr magico
    if somaT!=0 and somaF!=0:
        break
    b+=1



#--------------------------------------------------------------------------------------------------------------------------
#descobrir coluna
j = 0;i = 0;s = 0
while j < lado:
    
    if i < lado:
        s += square[i][j]
        i+=1
    else:
        if s == somaF:
            break
        j+=1;i = 0;s = 0


coordenadaerrada = square[linha][j]

if somaF > somaT:
    a = somaF - somaT #Valor a diminuir do numero erroneo para sair na primeira parte da saida.
    print(coordenadaerrada-a, coordenadaerrada)
else:
    a = somaT - somaF
    print(coordenadaerrada+a, coordenadaerrada)

