'''
O lobo mau e as ovelhas do Juvenal

Na fazenda de Juvenal existe um certo número de ovelhas. Enquanto elas estão
dormindo profundamente, alguns lobos famintos tentam invadir a fazenda e atacar as
ovelhas. Ovelhas normais ficariam indefesas diante de tal ameaça, mas felizmente as
ovelhas de Juvenal são praticantes de artes marciais e conseguem defender-se
adequadamente. A fazenda possui um formato retangular e consiste de campos
arranjados em linhas e colunas. Cada campo pode conter uma ovelha (representada pela
letra ‘k’), um lobo (letra ‘v’), uma cerca (símbolo ‘#’) ou simplesmente estar vazio (símbolo
‘.’). Consideramos que dois campos pertencem a um mesmo pasto se podemos ir de um
campo ao outro através de um caminho formado somente com movimentos horizontais ou
verticais, sem passar por uma cerca. Na fazenda podem existir campos vazios que não
pertencem a nenhum pasto. Um campo vazio não pertence a nenhum pasto se é possível
“escapar” da fazenda a partir desse campo (ou seja, caso exista um caminho desse
campo até a borda da fazenda). Durante a noite, as ovelhas conseguem combater os
lobos que estão no mesmo pasto, da seguinte forma: se em um determinado pasto houver
mais ovelhas do que lobos, as ovelhas sobrevivem e matam todos os lobos naquele
pasto. Caso contrário, as ovelhas daquele pasto são comidas pelos lobos, que
sobrevivem. Note que caso um pasto possua o mesmo número de lobos e ovelhas,
somente os lobos sobreviverão, já que lobos são predadores naturais, ao contrário de
ovelhas.
Tarefa
Escreva um programa que, dado um mapa da fazenda de Juvenal indicando a posição
das cercas, ovelhas e lobos, determine quantas ovelhas e quantos lobos estarão vivos na
manhã seguinte.
Entrada
A entrada contém um único conjunto de testes, que deve ser lido do arquivo de entrada. A
primeira linha da entrada contém dois inteiros R e C que indicam o número de linhas
(3<=R<=250) e de colunas (3<=C<=250) de campos da fazenda. Cada uma das R linhas
seguintes contém C caracteres, representando o conteúdo do campo localizado naquela
linha e coluna (espaço vazio, cerca, ovelha ou lobo).
Saída
Seu programa deve imprimir, no arquivo de saída, uma única linha, contendo dois inteiros,
sendo que o primeiro representa o número de ovelhas e o segundo representa o número
de lobos que ainda estão vivos na manhã seguinte.
--------------------------------------------------------------------------------------
Resolução:
'''
def acharcercas(area,i,j):
    global ovelhas,lobos,t
    if area[i][j] == 'k':
        ovelhas+=1
        area[i][j] = 'x' #marcar para n virar loop infinito com as recursões
        t+=1
    elif area[i][j] == 'v':
        lobos+=1
        area[i][j] = 'x'
        t+=1
    elif area[i][j] == 'x': #já marcado, entao n precisa
        return False
    elif area[i][j] == '#': #voltar p casa anterior
        return False  
    area[i][j] = 'x'
        
#---------------------------
    acharcercas(area,i-1,j)
    acharcercas(area,i,j-1)
    acharcercas(area,i+1,j)
    acharcercas(area,i,j+1)
    

l,c = map(int,input().split())
tO = 0;tL = 0;t = 0;area = []
for i in range(l):
    linha = list(input())
    area.append(linha)
##-----------    
for i in range(1,l): #ov e lob nunca na borda = sempre dentro de cercas!
    for j in range(1,c):
        if area[i][j] == 'v' or area[i][j] == 'k':
            lobos = 0;ovelhas = 0
            acharcercas(area,i,j)
            if t > 0:
                if lobos > ovelhas:
                    tL += lobos
                elif ovelhas > lobos:
                    tO += ovelhas
                else:
                    tL += lobos
print(tO,tL)
