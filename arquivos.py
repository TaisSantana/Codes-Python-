
def partition(l, p, r):
    pivot = l[r] #ultimo elemento da lista
    i = p-1#inicio da janelinha
    for j in range(p,r): #limite da janelinha
        if (l[j]) > (pivot):
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

#--------------------
pastas = []
n,b = map(int,input().split())
tamanhos = input().split()
tamanhos = [int(i) for i in tamanhos]
quicksort(tamanhos, 0, len(tamanhos)-1)
for x in tamanhos:
    if pastas == [] and x <= b:
        pastas.append([x,1])
    else:
        i = 0
        while i <len(pastas):
            if (pastas[i][0] + x) <= b and (pastas[i][1]) <= 2:
                pastas[i][0] += x
                pastas[i][1]+=1
                break
            else:
                i += 1
        else:
            pastas.append([x,1])

print(len(pastas))
