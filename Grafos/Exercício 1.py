# 1. Considere um grafo ponderado representado por listas de adjacência.
# Implemente uma função consulta_ligacoes(grafo, peso) que receba um grafo e
# um valor de peso e retorne todas as arestas cujo peso seja igual ao valor
# informado. A saída da função deve indicar: vértice de origem; vértice de
# destino; e peso da aresta.

def consulta_ligacoes(grafo, peso):
    for origem in grafo:
        for destino, p in grafo[origem]:
            if p == peso:
                print(f"{origem} -> {destino} ({p})")
 
# Grafo do enunciado
grafo = {
    'A': [('B', 5), ('C', 3)],
    'B': [('D', 5)],
    'C': [('D', 2)],
}
 
consulta_ligacoes(grafo, 5)

# Função adaptada

def consulta_ligacoes_desafio(grafo2, peso1, peso2):
    for origem in grafo2:
        for destino, p in grafo2[origem]:
            if p >= peso1 and p <= peso2:
                print(f"{origem} -> {destino} ({p})")
 
# Grafo do enunciado
grafo2 = {
    'A': [('B', 5), ('C', 3)],
    'B': [('D', 5)],
    'C': [('D', 2)],
}
 
consulta_ligacoes_desafio(grafo, 2,5)

