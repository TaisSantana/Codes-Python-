soma = 0
resultado=0
n = int(input())
qntdd = input().split()

#soma de todos os blocos nas pilhas.
for x in qntdd:
    soma += int(x)

#lista que representa a pilha com suas quantidades mínima possível de blocos para ser considerada escada perfeita.
minimo= [int(x)+1 for x in range(n)]
#soma dos valores da lista acima.
soma_minimo = (n*(n+1))/2
'''
# Para continuar tendo a propriedade de escada perfeita(diferença de 1 entre uma pilha e outra, sem criar ou remover pilhas)
# é necessário seguir o padrão de adicionar à cada pilha das pilhas iniciais exatamente +1, totalizando n a cada adição de blocos.
#O que valida se é ou não uma escada perfeita é se (a diferença entre a soma da entrada e a soma mínima) é divisível pela quantidade de pilhas (n)
#se for divisível, significa que é uma escada perfeita, então é feito os calculos para retornar o resultado.
#se não for divisível, não seguirá as regras, então deve imprimir -1.
'''

#verifica se é divisível
if  (soma - soma_minimo) % n == 0:

    #a é a quantidade de vezes que será possível adicionar +1 bloco a cada pilha.
    a = (soma - soma_minimo)/n

    for i in range(n):
        #b é a diferença entre a pilha dada pela questão e entre a pilha desejada no final para ser a escada perfeita.
        #A pilha desejada no final é o valor da pilha [inicial] +  a quantidade de vezes que adicionou +1 a cada pilha, ou seja, adicionado à a.
        b=(int(qntdd[i]) - int(minimo[i]+a))

        #É necessário essa comparação pois se o valor de b for negativo, não é necessário pôr na conta, visto que, serão os valores que serão retirados
        #para dar o formato da escada perfeita. E se coloca-los em consideração, a variável resultado sempre dará zero.
        if b > 0:
             resultado+= b
    print(resultado)
else:
    print(-1)
