'''
Strings bem formadas

Pilhas e filas são geralmente consideradas estruturas de dados básicas e podem ser empregadas em sistemas operacionais, simulações discretas de eventos, dentre outros. As pilhas são muito importantes também na teoria da computação / linguagens formais. Neste exercício, você deverá implementar um algoritmo automatizado para identificar se os parênteses, colchetes e chaves estão sendo utilizados corretamente em um texto. Dado um texto de entrada, você deverá escrever um programa em python 3 que verificará se uma string é bem formada. 
Uma string é bem formada quando seus delimitadores (parênteses, colchetes e chaves) à esquerda possuem os correspondentes à direita na ordem de ocorrência inversa. Exemplos de strings bem formadas: 
• bsi [ ufrpe { recife ( dois ) mil }aaaa]kkk 
• huuuumm{}asa[ssd]fox{}(asas{ss}) 
• sddssdds 
• ( ( ) [ ( ) ] ) 
• [ ] ( ) [ ] 
• ( ( [ ] ) [ ( ) ] ) [ ( ) ] 
Exemplos de strings mal formadas:
• essa(nao[ta muito) legal ] ne 
• tem{coisa{a{mais}aqui}ne}kkkk} 
• ( [ ) ] 
• ( [ ] ) ]
• ( ( ) [ ] 
Entrada A única linha da entrada terá a string a ser verificada. Você deverá usar a função input() do python 3. Saída A saída deverá imprimir (print) uma das duas opções a seguir: “string bem formada” ou “string mal formada”. Não use aspas. Não imprima espaços extras antes ou depois do texto.

------------------------------------------------------------------------
Resolução:

Observações:
1- Último que abre é o primeiro que fecha.
2- Sempre quando vai fechar o último aberto o seu par se localiza na próxima posição.

-Sempre que achar um abre-algo: Empilha.
- Sempre que achar um fecha-algo: Compara se o último elemento da pilha(Top) é o seu par, se for exclui o último elemento da pilha.
#Sobre a comparação se o tamanho da pilha for maior que 0: Por que se tivesse comparações como: {{}}} ou ()) ,por causa da última condicional, sempre dava certo, então foi necessário essa condicional adicionada ao fecha-algo que sobra na pilha.


'''

sequence = input()
stack = []
for i in sequence:
    if i == "(" or i == "[" or i == "{":
        stack.append(i)

    elif i == ")":
        if len(stack) > 0:
            if stack[-1] == "(":
                stack.pop(-1)
            else:
                stack.append(i)
                break
        else:
            stack.append(i)
            break
    elif i == "]":
        if len(stack) > 0:
            if stack[-1] == "[":
                stack.pop(-1)
            else:
                stack.append(i)
                break
        else:
            stack.append(i)
            break
    elif i == "}":
        if len(stack) > 0:
            if stack[-1] == "{":
                stack.pop(-1)
            else:
                stack.append(i)
                break
        else:
            stack.append(i)
            break
    

if len(stack) == 0:
    print("string bem formada")
else:
    print("string mal formada")


