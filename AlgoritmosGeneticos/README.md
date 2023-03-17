# Experimentos de otimização e algoritmos genéticos

Glossário das atividades, esse material foi retirado do notbook feito por Daniel Cassar:

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
