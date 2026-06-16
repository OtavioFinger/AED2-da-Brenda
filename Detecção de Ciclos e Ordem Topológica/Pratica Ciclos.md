
# Detecção de Ciclos e Ordem Topológica

Ciclos: É quando um caminho começa e termina no mesmo vértice, passando por arestas e vértices no meio.
Podemos até acabar em um nó destino, mas podemos fazer uma volta em um ciclo desnecessário que acaba dando mais peso desnecessário.

*Obs: Um grafo não direcionado é efetivamente um ciclo de ida e volta!*

# Algoritmos para resolver o problema

## Busca em Profundidade (DFS) com Pilha de Recursão

    A detecção utiliza uma pilha de recursão para rastrear o caminho atual do percurso.

    Exemplo de Estados dos nós:
        Campo de Cores:
        [] Branco: Não visitado.
        [] Cinza: Visitado, mas ainda na pilha (em processamento).
        [] Preto: Processado e finalizado.

    Se DFS encontrar um nó que já está **CINZA**, um ciclo foi **DETECTADO**.


## Algoritmo de Kahn (Baseado em Ordenação Topológica)
