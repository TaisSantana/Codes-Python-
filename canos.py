def rearranjar(i):
    return [i]
def partition(l, p, r):
    pivot = l[r][1] #ultimo elemento da lista
    i = p-1#inicio da janelinha
    for j in range(p,r): #limite da janelinha
        if rearranjar(l[j][1]) <= rearranjar(pivot):
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


def mochila_inteira(n,sobra,l):
    if n ==0 or sobra ==0:
        return 0
    elif l[n][0] > sobra:
        return mochila_inteira(n-1,sobra,l)
    else:
        usa = l[n][1] + mochila_inteira(n-1,sobra-l[n][0],l)
        naousa = mochila_inteira(n-1,sobra,l)
        return max(usa,naousa)

l = [];resultado=0
n,tam_cano = map(int,input().split())
sobra = tam_cano #var q vai subtraindo pelo tam

for x in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
print(l)
quicksort(l, 0, n-1)
print(l)
print(mochila_inteira(n-1,tam_cano,l))
