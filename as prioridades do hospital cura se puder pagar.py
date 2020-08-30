def rearranjar(l):
    return [-l[0],-l[1],l[2]]
def partition(l, p, r):
    pivot = l[r] #ultimo elemento da lista
    i = p-1#inicio da janelinha
    for j in range(p,r): #limite da janelinha
        if rearranjar(l[j]) <= rearranjar(pivot):
            i +=1 #afasta janelinha para direita
            l[i],l[j] = l[j],l[i]
    l[i+1],l[r] =l[r],l[i+1] #muda o pivot
    return i+1 #retorna indice do pivot
#esq i+1 é menor q ele, e dir de i+1 é maior q ele.
        


def quicksort(l, p, r):
    if p < r:
        q = partition(l, p, r)#retorna indice do novo pivot
        quicksort(l, p, q-1)#ordena todos q são menor que pivot
        quicksort(l, q+1, r)#ordena todos q são maiores q pivot

#entrada-------------------------------------------------------------
def planos(nome,plano, urgencia, l):
    if plano == "premium":  plano = 10
    elif plano == "diamante": plano = 9
    elif plano == "ouro": plano = 8
    elif plano == "prata":  plano = 7
    elif plano == "bronze":  plano = 6
    elif plano == "resto": plano = 5

    l.append((plano, (urgencia),(nome)))
    return l

qtd = int(input())
lista = []
for x in range(qtd):
    paciente = input().split()
    nome,plano,urgencia = paciente[0],paciente[1],int(paciente[2])
    planos(nome, plano, urgencia,lista)
r = qtd-1
p = 0
quicksort(lista,p,r)

for x in range(qtd):
    print(lista[x][2])
