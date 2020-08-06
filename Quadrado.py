
lado = int(input()) #qntdd lados
square = [list(map(int,input().split())) for x in range(lado)] #formando linhas da matriz que forma o quadrado.
listasomas = []#lista p guardar somas e desc a soma True. 

for e in square:
    listasomas.append(sum(e))


b = 0 #indica a linha p coordenada errada do final
somaT = 0;somaF = 0
for elem in listasomas: #cada soma corresponde ao msm num da linha 
    if listasomas.count(elem) == 1 :
        somaF = elem #soma equivocada
        linha = b
    elif listasomas.count(elem) != 1 : 
        somaT = elem #valor correto da soma do sqr magico
    if somaT!=0 and somaF!=0:
        break
    b+=1



#--------------------------------------------------------------------------------------------------------------------------
#descobrir coluna
j = 0;i = 0;s = 0
while j < lado:
    
    if i < lado:
        s += square[i][j]
        i+=1
    else:
        if s == somaF:
            break
        j+=1;i = 0;s = 0


coordenadaerrada = square[linha][j]

if somaF > somaT:
    a = somaF - somaT #Valor a diminuir do numero erroneo para sair na primeira parte da saida.
    print(coordenadaerrada-a, coordenadaerrada)
else:
    a = somaT - somaF
    print(coordenadaerrada+a, coordenadaerrada)

