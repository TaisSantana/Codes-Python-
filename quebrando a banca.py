'''
Quebrando a Banca

Juvenal e seu parceiro Leôncio estavam voltando para casa quando receberam uma
ligação de Tobias, gerente do banco a qual são clientes. Tobias falou que houve
um grande problema no saldo de usuários do banco: foram, acidentalmente,
concatenados (em posições aleatórias) inteiros em cada saldo e não existe um
backup para se descobrir o valor antigo, mas o banco sabe quantos caracteres
foram concatenados em cada saldo.
Para resolver a situação o banco resolveu retirar caracteres do saldo. Juvenal,
que não ia aceitar perder dinheiro, obrigou o banco a deixar o saldo o maior
possível quando se retirassem os caracteres.
Por exemplo, se eu sei que o saldo é 1435 e sabendo que existem 2 caracteres
extras nesse saldo, posso concluir que devo apagar os números 1 e 3 para gerar o
maior saldo possível: 45.
Leôncio conhece (superficialmente) os conceitos de Estruturas de Dados, logo
precisa de sua ajuda para descobrir as maiores sequências possíveis que podem
ser formadas ao se retirar caracteres.

Formato de Entrada
Vão existir vários casos de teste. (use endOfFile)
Cada caso é formado por A e B 1 <= B < A <= 10^5 seguido na linha abaixo por A
caracteres (o primeiro digito nunca vai ser zero) que representam inteiros, B é
a quantidade de dígitos que você deve apagar.

Formato de Saída
Imprima o maior saldo possível que pode existir depois da retirada de
caracteres.
'''
#Verifica parcialmente, um dígito de cada vez.
maior = 0
while True:
    try:
        a,b = map(int,input().split())
        saldo= input()
        
        if a == b:
            saldo = "0"
        else:
            #loop executa  = qntdds de digitos a ser apagados.
            for i in range(b):
                #O segundo loop compara todos os valores possíveis se retirar um dos dígitos,
                #para descobrir qual o maior valor possível dada a ordem da entrada.
                for j in range(len(saldo)):
                    atual = saldo[:j]+saldo[j+1:]
                    if int(atual) > maior:
                        maior = int(atual)
                #saldo é atualizado pelo maior resultado do valor inicial - o número retirado
                saldo = str(maior)
                #maior reseta para não dar erro na comparação acima,
                #e então imprimir sempre o resultado da primeira interação
                #(pq o valor da 1 iteração smpr vai ser maior q as próximas).
                maior = 0
        print(int(saldo))
    except EOFError:
        break
