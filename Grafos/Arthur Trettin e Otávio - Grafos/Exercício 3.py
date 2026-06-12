# Implemente uma função que determine se todos os vértices de um grafo são
# alcançáveis a partir de um vértice inicial. Utilize BFS ou DFS para realizar a
# verificação. A função deve retornar:
# - "Conexo" caso todos os vértices sejam visitados;
# - "Não conexo" caso existam vértices não alcançáveis.

def bfs(grafo, inicio):

    visitados = []
    fila = [inicio]
    vistos = {inicio}

    while fila:
        vertice = fila.pop(0)   # remove o primeiro da fila
        visitados.append(vertice)

        for vizinho in grafo.get(vertice, []):
            if vizinho not in vistos:
                vistos.add(vizinho) #descobri
                fila.append(vizinho) # visitarei depois
 
    return visitados

def verifica_conexo(grafo, inicio):

    visitados = bfs(grafo, inicio)

    if len(visitados) == len(grafo):
        return "Conexo, todos os vértices foram visitados"
    else:
        return "Não conexo, há vértices n-alcançáveis"


# Exemplo conexo
grafo1 = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [8, 9],
    6: [10],
    7: [],
    8: [11],
    9: [11],
    10: [],
    11: [12],
    12: []
}

grafo2 = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [8, 9],
    6: [10],
    7: [],
    8: [11],
    9: [11],
    10: [],
    11: [12],
    12: [], # Daqui pra baixo sem relação com o resto
    13: [14],
    14: [15],
    15: []
}

inicio = int(input("Informe o vértice inicial: "))

print("Grafo 1:", verifica_conexo(grafo1, inicio))
print("Grafo 2:", verifica_conexo(grafo2, inicio))


