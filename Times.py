'''

Times

Juvenal sempre foi escolhido por último nas aulas de educação física. Não importava se
quem escolhia os times eram os alunos ou o professor, ele sempre era relegado. A
escolha dos times ocorria da seguinte maneira: O professor entrega uma bola aos alunos
(geralmente de futebol) e estes se dividem em times, onde jogam partidas
alternadamente. A maneira como os times são escolhidos também é semelhante em todas
as escolas: decide-se quantos times serão formados, e uma pessoa para montar cada um
dos times. Cada pessoa vai escolher, alternadamente, um dos alunos restantes para fazer
parte de sua equipe. Como todos querem ter uma boa equipe, a pessoa que vai escolher
o próximo membro do time escolhe aquele, dentre os ainda disponíveis, que possui o
melhor nível de habilidade. Assim, os times acabam ficando relativamente equilibrados na
soma do nível de habilidade dos jogadores.
Tarefa
No entanto, só para reforçar o estereótipo, Juvenal sempre foi o primeiro a ser escolhido
para desenvolver sistemas computacionais. O seu antigo professor de educação física
pediu para ele escrever um programa que, dada uma lista de alunos que serão escolhidos
e seus respectivos níveis de habilidade para os times e a quantidade de times que serão
formados. Ajude Juvenal a realizar essa tarefa e mostre como ficarão os times ao final do
processo de montagem dos mesmos.
Entrada
A primeira linha da entrada contém dois inteiros N (2≤N≤10.000) e T (2 ≤T≤1000),
representando respectivamente a quantidade de alunos e o número de times a serem
formados, sendo T≤N. As N linhas seguintes descrevem, cada uma, um aluno disponível
para escolha de times. Cada uma dessas linhas possui o nome do aluno (composto
apenas por letras minúsculas) e um inteiro H(0 ≤H≤1.000.000) descrevendo seu nível de
habilidade). Não existem dois alunos com o mesmo nível de habilidade, e todos eles
possuem nomes diferentes. É possível que alguns times acabem ficando com menos
jogadores do que os outros.
Saída
Seu programa deve imprimir a lista de times que será formada ao final do processo de
seleção. Para cada time, você deverá mostrar o termo “Time N”, onde N é o número do
time (1 para o primeiro, 2 para o segundo, e assim por diante) seguido de K linhas, onde
K é a quantidade de jogadores do time, mostrando o nome de cada um dos jogadores do
time, em ordem alfabética. Imprima uma linha em branco após cada descrição de time
(inclusive do último). Os times serão escolhidos pelo computador, então não é necessário
considerar o aluno que fará a escolha dos times
-------------------------------------------------------------------------------------------

Resolução:
'''
a,t = map(int,input().split()) #qntd alunos e de times.
dic = {};lista = []
for x in range(a):
    b = input().split()
    nome = b[0]
    lvl = int(b[1])
    dic[lvl] = nome
    lista.append(lvl)

lista.sort()
#lista de pessoas--------------------------------------------
times = [] #matriz contendo nomes dos participantes dos 3 times
for x in range(t):
    times.append([]) #lista dentro da maior lista, p armazenar participantes de cada time.
while len(lista) > 0:
    for x in times:
        try:
            x.append(dic[lista[-1]])
            del lista[-1]
        except:
            break
        x.sort()

#-------------------------------------------------------------------
i=0
for x in times:
    print('Time',i+1)
    for j in range(len(x)):
        print(times[i][j])    
    print()
    i+=1
    
