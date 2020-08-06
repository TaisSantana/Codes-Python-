'''
Cálculo de complexidade 

Analisar a complexidade de tempo de execução de um algoritmo é uma tarefa muito importante para a criação de programas eficientes. Um algoritmo que executa em tempo linear é geralmente muito mais rápido que um algoritmo que necessita de tempo exponencial para a mesma tarefa. Geralmente, o tempo de execução de um algoritmo é definido de acordo com o tamanho N da entrada, onde N pode ser a quantidade de elementos a serem ordenados, o número de pontos de determinado polígono e assim por diante. Desta forma, determinar uma fórmula para o tempo de execução em função de N não é uma tarefa simples e seria muito bom se isso fosse automatizado. Infelizmente, isto em geral não é possível, mas neste exercício você irá considerar programas de natureza simples e poderá determinar a quantidade de operações de um programa com precisão. 

Nossos programas de entrada serão criados de acordo com as regras abaixo (dadas na BNF), onde pode ser qualquer número inteiro não-negativo. 
• ::= “INICIO” “FIM” 
• ::= “LOOP” <numero> “FIM” 
• ::= “OP” <numero>

O tempo de execução de um programa deverá ser calculado da seguinte maneira: 
• a execução de uma Declaracao-OP custa a quantidade de tempo especificada pelo seu parâmetro (considere que OP é uma operação que será realizada com o custo informado);
 • a lista de declarações dentro de um LOOP será realizada tantas vezes quantas estiverem indicadas no parâmetro ;
 • o tempo de execução de uma lista de declarações é a soma das quantidades de tempo das partes que a compõem. 
REGRA GERAL: Você deverá utilizar obrigatoriamente pilhas em python 3 implementadas em listas com acesso permitido somente às funções: append, pop e len. Sempre que um novo loop for fechado, a quantidade de operações que foi calculada dentro dele deverá ser multiplicada pela quantidade de vezes que o loop executou. Note que é possível ter loops aninhados em múltiplos níveis.

 Entrada A entrada contém um programa que é construído de acordo com a gramática acima. Espaços em branco, tabulações e quebras de linha (\r e \n) podem aparecer em qualquer local do programa e devem ser desconsiderados, mas não aparecerão dentro das palavras INICIO, FIM, LOOP, OP e nem dentro de um número inteiro. A profundidade dos operadores do LOOP será de no máximo 10. Por questões técnicas da plataforma de testes, toda a entrada será lida em uma única linha sem enter.

 Saída A saída deverá exibir o tempo de execução como um número inteiro. 


------------------------------------------------------------------------

Resolução:

FIM - pode ser do Loop ou do programa!

-Adc coisas na pilha até achar a palavra “FIM”
-Qnd achar desempilhar até chegar na palavra “LOOP” ou “INICIO”
-Enqnt desempilha somar

INICIO OP 199 LOOP 10 LOOP 10 OP 1 FIM FIM FIM
INICIO	LOOP 10 OP 4 LOOP 3 LOOP 5 OP 1 FIM OP 2 FIM OP 1	FIM OP 17 FIM

INICIO LOOP 2 FIM LOOP 5 OP 10 OP 10 FIM FIM
INICIO LOOP 2
resultado = 2
INICIO LOOP 5 OP 10 OP 10
resultado = 22
INICIO LOOP 5
resultado = 110
INICIO 
resultado = 110
------------------------------------------------------------------------
'''
entrada = input().split()
stack = []
ant = 0;resultado = 0
for i in entrada:
   
    if i != "FIM":
        stack.append(i)
    else:
        while True:
            atual = stack.pop(-1)#elemento aa ser verificado na pilh
            if atual == "OP":
                resultado += int(ant)
                
            elif atual == "LOOP":
                if resultado != 0: #significa que a var resultado não é 0. pois se for, a multip sempre dará 0.
                    resultado *= int(ant)
                    
                else:
                    resultado = int(ant)
                break
                    
               
            elif atual == "INICIO":
                print(resultado)
                break

            else: #se for número
                ant = atual #É O QUE TEM NA ULTIMA EXCLUSAO
                

      
            



