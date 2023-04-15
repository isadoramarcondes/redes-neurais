# Experimentos de otimização e algoritmos genéticos
<p align="justify">
Este é um repositório dedicado ao estudo de algoritmos genéticos. Aqui você encontrará recursos e materiais para ajudá-lo a entender e implementar algoritmos genéticos em seus próprios projetos. Os algoritmos genéticos são uma técnica de otimização baseada em princípios evolutivos. Eles foram inspirados pela seleção natural e reprodução dos seres vivos e podem ser usados para encontrar soluções para problemas complexos e multidimensionais.
<p align="justify">
Aqui você encontrará exemplos de implementação de algoritmos genéticos em diferentes problemas, como o problema do caixeiro viajante e a otimização de parâmetros de modelos de aprendizado de máquina.

- `experimento A.01 - busca aleatoria`
O problema das caixas binárias é simples: nós temos um certo número de caixas e cada uma pode conter um valor do conjunto $\{0, 1\}$. O objetivo é encontrar uma combinação de caixas onde a soma dos valores contidos dentro delas é máximo. Como todo problema computacional, um dos desafios é "traduzir" o problema dado em estruturas computacionais. Usamos busca aleatória para resolver o problema.

- `experimento A.02 - busca em grade`
Usamos busca em grade para solucionar o problema das caixas binárias.


- `experimento A.03 - algoritmo genetico`
Encontrar uma solução para o problema das caixas binárias usando o algoritmo genético. Consideramos 4 caixas. Repare que o problema é o mesmo que o anterios, com a diferença que usamos a abordagem dos algoritmo genético


- `experimento A.04 - caixas nao-binarias`
O problema das caixas não-binárias consistem em um certo número de caixas e cada uma pode conter um número inteiro. O objetivo é encontrar uma combinação de caixas onde a soma dos valores contidos dentro delas é máximo.

- `experimento A.05 - descobrindo a senha`
Usar um algoritmo genético para descobrir uma senha. Neste problema, a função objetivo deve saber a senha correta e quantificar de alguma maneira o quão perto ou longe os palpites estão da solução. O critério de parada deste problema é quando a senha for descoberta.

- experimento A.06 - o caixeiro viajante
O problema consiste em descobrir a rota de menor distância entre $n$ pontos no plano cartesiano (ou seja, $n$ pontos com coordenadas $(x,y)$). A rota pode se iniciar em qualquer um dos pontos disponíveis e deve terminar no ponto inicial, visitando todos os demais pontos apenas uma vez. Considere que a rota entre um ponto e outro é a linha reta que liga os dois pontos.

- `experimento A.07 - aplicando restricoes`
O problema da mochila envolve encontrar um conjunto de itens de um número que definimos em nosso dicionário, cada um com um peso e valor associado, que maximize o valor total contido na mochila, considerando a capacidade limitada da mesma



<details><summary><h3><b>Glossário das atividades, esse material foi retirado do notbook feito por Daniel Cassar <a href="https://github.com/drcassar"> (@drcassar)</a>:</h3></b></summary>

-   `Indivíduo`: um candidato para a solução do problema;

-   `População`: um conjunto de candidatos para a solução do problema;

-   `Gene`: um parâmetro que pertence a um indivíduo;

-   `Cromossomo` ou `genótipo`: um conjunto de genes;

-   `Geração`: cada população em uma busca genética faz parte de uma geração. A primeira geração é geralmente formada por indivíduos aleatórios (sorteados dentro do espaço de busca). As gerações seguintes são formadas por seleção, cruzamento e mutação da geração anterior. Um dos critérios de parada possíveis para um algoritmo genético é o número máximo de gerações;

-   `Função de aptidão` ou `função objetivo` ou `função fitness`: uma função que recebe um indivíduo e retorna o seu valor de aptidão. Em um problema de otimização, nós buscamos encontrar soluções que minimizam ou maximizam o valor de aptidão;

-   `Seleção`: processo onde utilizamos o valor de aptidão dos indivíduos para selecionar quais irão passar seus genes para a geração seguinte;

-   `Cruzamento`: processo onde o material genético de indivíduos selecionados é misturado;

-   `Mutação`: processo onde os genes dos indivíduos selecionados têm uma chance de alterar seu valor. A mutação é o único processo capaz de introduzir informação nova ao pool genético após o sorteio aleatório da primeira geração;

-   `Hall da fama`: conjunto dos $n$ indivíduos que obtiveram os melhores valores de aptidão durante o processo de busca.
