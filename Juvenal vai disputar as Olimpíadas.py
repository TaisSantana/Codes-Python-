def rearranjar(l):
    return [l[0],l[1],l[2],-l[3]]
def partition(l, p, r):
    pivot = l[r] #ultimo elemento da lista
    i = p-1#inicio da janelinha
    for j in range(p,r): #limite da janelinha
        if rearranjar(l[j]) >= rearranjar(pivot):
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
n,m = map(int,input().split())
#[ouro,prata,bronze,id_pais]
matriz = [[0,0,0,x+1] for x in range(n)]

for i in range(m):
    g,p,b = map(int,input().split())
    matriz[g-1][0]+=1
    matriz[p-1][1]+=1
    matriz[b-1][2]+=1

p=0
r=n-1
quicksort(matriz,p,r)
result= ''
for i in range(len(matriz)):
    if i < (len(matriz) - 1):
        result += str(matriz[i][3]) + ' '
    else:
        result += str(matriz[i][3]) 
print(result)



