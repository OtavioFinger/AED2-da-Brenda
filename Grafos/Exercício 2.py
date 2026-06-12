# Considere a árvore binária qualquer, agora representada como um grafo por
# meio de listas ou matriz de adjacência.
# Implemente os algoritmos: Busca em Largura (BFS) e Busca em
# Profundidade (DFS). Para ambos os algoritmos:
# a. Receba um vértice inicial informado pelo usuário.
# b. Exiba a ordem de visitação dos vértices.


def bfs(grafo, inicio):

    visitados = [] # guarda os nós já visitados
    fila = [inicio] # na verdade é uma fila de duas-pontas
    vistos = {inicio}

    while fila:
        vertice = fila.pop(0) # "tira" do começo
        visitados.append(vertice)

        for vizinho in grafo.get(vertice, []):
            if vizinho not in vistos:
                vistos.add(vizinho)
                fila.append(vizinho)

    return visitados

def dfs(grafo, inicio, visitados=None):

    if visitados is None:
        visitados = []
    visitados.append(inicio)

    for vizinho in grafo.get(inicio, []):
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)
    return visitados


# Árvore binária do exemplo (obrigado gpt):
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

grafo = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: [],
}

inicio = int(input("Informe o vértice inicial: "))

print("BFS (Busca por Largura):", bfs(grafo, inicio))
print("DFS (Busca por Profundidade):", dfs(grafo, inicio))

# Desafios abaixo (perguntar Prof Brenda)
