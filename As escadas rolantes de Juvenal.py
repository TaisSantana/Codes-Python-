'''
As escadas rolantes de Juvenal

Juvenal ganhou na loteria e agora é dono de um shopping: o JuvenaMall. Como relatado
anteriormente, ele tem preocupação com o meio ambiente. Nosso protagonista está preocupado
com o consumo de energia e, resolveu trocar todas as escadas rolantes por modelos mais modernos,
que se desligam caso ninguém esteja utilizando, poupando energia.
A nova escada rolante possui um sensor no início. Toda vez que ela está vazia e alguém passa pelo
sensor, a escada começa a funcionar, parando de funcionar novamente após 10 segundos se
ninguém mais passar pelo sensor. Estes 10 segundos representam o tempo suficiente para levar
alguém de um nível ao outro.
Preocupados em saber exatamente quanto de energia o shopping está economizando, o gerente
pediu sua ajuda. Como eles sabem qual era o consumo da escada rolante antiga, eles te pediram
para calcular o tempo que a nova escada ficou funcionando.

Tarefa

Dados os instantes, em segundos, em que passaram pessoas pela escada rolante, você deve calcular
quantos segundos ela ficou ligada.

Entrada

A primeira linha da entrada contém um inteiro N que indica o número de pessoas que o sensor
detectou (1≤N≤1.000). As N linhas seguintes representam o instante em que a i-ésima pessoa passou
pelo sensor e contém um inteiro T (0≤T≤10.000). Os tempos estão em ordem crescente, sem
repetições.
Saída
Seu programa deve imprimir uma única linha, contendo o tempo que a escada rolante ficou ligada.

--------------------------------------------------------------------------------------------------

Resolução:
'''

#A escada só desliga depois de 10s SE alguém não passar antes
#Sempre que alguem passar pelo sensor inicial da escada rolante o tempo de 10s reinicia, que é representado pela variavel flag.
#Se o tempo que a pessoa passar for antes de 10s, ou exatamente 10s, a escada está ligada, então o tempo é contabilizado 
ant = 0
flag = 0
soma_tempo = 0
n = int(input())
for i in range(n):
    tempo_passagem = int(input())

    if tempo_passagem <= flag:
        soma_tempo+= (tempo_passagem - ant)
    #else falha p 1x
    #geralmente da 10, que é o tempo q a escada fica ligada dps q alguém passa (dps de 10s)
    else:
        soma_tempo += flag - ant 
    
    ant = tempo_passagem
    flag = tempo_passagem + 10

# e se der false o if, testar
soma_tempo+=10
print(soma_tempo)
