'''
Linhas Cruzadas

Uma das atividades de recreação preferidas de Letícia é compor desenhos com linhas
coloridas esticadas entre preguinhos numa base de madeira. Quanto mais cruzamentos
entre pares de linhas, mais interessante fica a figura. Neste problema temos N pregos na
vertical e N pregos na horizontal, como na figura abaixo. Os pregos na vertical possuem
uma numeração fixa, de 1 a N, de baixo para cima. Os pregos na horizontal também são
numerados de 1 a N, mas a ordem pode ser qualquer uma. Letícia vai sempre esticar uma
linha entre cada par de pregos que tiverem o mesmo número. Dada a ordem dos pregos
horizontais, seu programa deve computar o número total de cruzamentos entre pares de
linhas no desenho de Letícia. Por exemplo, os três desenhos da figura possuem,
respectivamente, 0, 6 e 15 cruzamentos.

Entrada
A primeira linha da entrada contém um número natural N. A segunda linha contém N
números naturais distintos de 1 a N, representando a ordem dos pregos na horizontal.

Saída
Seu programa deve escrever uma linha na saída, contendo o número de cruzamentos
entre pares de linhas, conforme a descrição anterior.
----------------------------------------------------------------------------------
Resultado:
'''

n = int(input())
l = list(map(int,input().split()))
a = 0;cruzamentos = 0
while a < n-1:
    for i in range(1+a,n):
        if l[a] > l[i]:
            cruzamentos += 1
    a+=1
print(cruzamentos)
