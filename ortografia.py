def minimo(x,y,z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    else:
        return z
def distancia_de_edicao(M,word1,word2):
    c=0
    for i in range(1,len(word1)+1):
        for j in range(1,len(word2)+1):
            if word1[i-1] == word2[j-1]:
                c = 0
            else:
                c = 1
            M[i][j] = minimo(M[i-1][j-1] + c, M[i-1][j] +1, M[i][j-1] + 1)
    return M[len(word1)][len(word2)]

def arrumar(M,word1,word2):
    for i in range(len(word1)+1):
        M[i][0] = i
    for j in range(len(word2)+1):
        M[0][j] = j
    return M 

dic = []
analisar = []
n,m = map(int,input().split())
result=[[] for i in range(m)]

for x in range(n):
    a = input()
    dic.append(a)
for x in range(m):
    a = input()
    analisar.append(a)
#para cada palavra em dic e cada palavra em analisar


for x in dic:
    b=0
    for y in analisar:
        M = [[0]*(len(x)+1) for a in range(len(y)+1)]
        arrumar(M,y,x)
        a = distancia_de_edicao(M,y,x)
        if a <= 2: 
            result[b].append(x)
        b+=1
for x in result:
    print(' '.join(x))
            
            
            
        
        


        
        
        
        
        
