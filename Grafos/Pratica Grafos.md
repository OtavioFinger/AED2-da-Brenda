# Grafos

## Introdução 

Um grafo é definido por G(V,A)
- V é um conjunto de vértices (nós)
- A é um conjunto FINITO de arestas

*Obs: Uma aresta pode conter um peso, que define seu custo até o nodo o qual ele é relacionado.*

São estruturas matemáticas que representam relações entre objetos(nodos).

### Problemas interessantes:

1. 6 Graus de Separação
2. As 7 Pontes de Königsberg (1736): Königsberg (atual K            aliningrado) possuía duas
    ilhas ligadas por sete pontes. O desafio era
    atravessar todas sem repetir nenhuma

## Conceitos Básicos

● Um grafo com nenhum vértice: vazio
● Um vértice com nenhuma aresta: isolado
● Um vértice associado a uma aresta: terminal
● Função associando terminais: aresta-vértice
● Aresta com somente um terminal: laço
● Arestas dos mesmos vértices são: paralelas
● Vértices conectados pela aresta: adjacentes
● Quantidade de arestas do vértice: grau

## Representações

Para se representar um grafo, existem duas formas de analisar quais dos seus nós (vértices) possuem conexões entre si:

### Matriz de Adjacência:

É formada pelo (n.vértices)². Assim, se usa 0 e 1 para saber se eles estão relacionados. 
    0 para N-RELACIONADO.
    1 para RELACIONADO.

Quando usar? Grafos Densos, Grafos Esparsos(mais nós que arestas), Testar Existência entre arestas, Encontrar nós que possuam ligação antes.

### Lista de Adjacência:

    Consiste em uma lista onde cada elementos é um nó do grafo.
    TAM.LISTA = N. DE VÉRTICES DO GRAFO.

    Essa lista possui listas-extras para cada nodo. Contém a conexão por arestas

    *Obs: Vira um VETOR de LISTAS.*
    [V1]->[V2]->[V4]->NULL (v1 tem aresta para v2 e v4)

**Quando usar?** Busca

## Grafos NÃO-Ponderados

As arestas não possuem valor em específico. Tem o mesmo custo uniforme.
Todas as arestas são IGUAIS.

## Grafos Ponderados (mais útil)

As arestas possuem um peso(valor númerico) associado.
Peso pode ser custo, tempo, distância,etc.

**Exemplos:** Rotas de entrega, Rede de Telecomunicações.

Em vez de 0 e 1, agora teremos o próprio valor de custo do Nodo X para Y.

<img src="https://medium.com/@paulomartins_10299/grafos-representa%C3%A7%C3%A3o-e-implementa%C3%A7%C3%A3o-f260dd98823d" width="300" height="200" alt="Grafos — representação e implementação por Paulo Martins">