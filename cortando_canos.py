def maximo(x,y):
    if x > y:
        return x
    else:
        return y
def mochila(T,l,n,c):
    for j in range(1,c+1):
        for i in range(1,n+1):
            if l[i-1][0] > j:
                T[i][j]= T[i-1][j]
            else:
                T[i][j]= maximo(T[i-1][j],(T[i-1][j-l[i-1][0]])+l[i-1][1])
    return T[n][c]
                


l = []
n,c = map(int,input().split())
T = [[0]*(c+1) for a in range(n+1)]
for x in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
print(mochila(T,l,n,c))

        
        


        
        
        
        
        
