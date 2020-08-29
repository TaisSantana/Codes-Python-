soma=0;somaent=0
n = int(input())
ent = input().split()
'''
comp = [int(x) for x in range(1,n+1)]

for i in comp[:]:
    #compara numero atual com todos valores dentro de ent,
    #se corresponder, exclui esse valor da lista comp p
    for x in ent[:]:
        if i == int(x):
            comp.remove(i)
            break
print(comp[0])
 O algoritmo acima é O(n^2), para ser O(n):
# somar cada termo e dps subtrair um pelo outro'''
for x in range(1,n+1):
    soma += x
for x in ent:
    somaent += int(x)
print(soma - somaent)

     
    

        
            
            
        
        
    
    
