'''
Botas Trocadas

A divisão de Suprimentos de Botas e Calçados do Exército comprou um grande número
de pares de botas de vários tamanhos para seus soldados. No entanto, por uma falha de
empacotamento da fábrica contratada, nem todas as caixas entregues continham um par
de botas correto, com duas botas do mesmo tamanho, uma para cada pé. O sargento
mandou que os recrutas retirassem todas as botas de todas as caixas para reembalá-las,
desta vez corretamente. Quando o sargento descobriu que você sabia programar, ele
solicitou com a gentileza habitual que você escrevesse um programa que, dada a lista
contendo a descrição de cada bota entregue, determina quantos pares corretos de botas
poderão ser formados no total.

Entrada
A primeira linha da entrada contém um inteiro N indicando o número de botas individuais
entregues. Cada uma das N linhas seguintes descreve uma bota, contendo um número
inteiro M e uma letra L, separados por um espaço em branco. M indica o número do
tamanho da bota e L indica o pé da bota: L = ‘D’ indica que a bota é para o pé direito, L =
‘E’ indica que a bota é para o pé esquerdo.

Saída
Seu programa deve imprimir uma única linha contendo um único número inteiro indicando
o número total de pares corretos de botas que podem ser formados.
Restrições
 2<-N<=104
 N é par
 30<=M<=60
 L é o caractere ‘D’ ou o caractere ‘E’
 ---------------------------------------------------------------------------------------------
 Resolução:
 '''
n = int(input()) #n botas individuais
l = [list(map(str,input().split())) for x in range(n)]

pares = 0               #len(l)+1)-i
i = 0
a = len(l)
while i < len(l): #
    try:
        for x in range(1+i,a):
            if l[i][0] == l[x][0]:
                if l[i][1] != l[x][1]:
                    pares+=1
                    del l[x]
                    a = len(l)
                    break
        i+=1
    except:
        break             
                
    
print(pares)

