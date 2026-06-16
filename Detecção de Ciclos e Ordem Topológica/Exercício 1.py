# Exercício 1*. Você foi selecionado como bolsista institucional para ajudar o NRC a dar
# suporte aos labs da computação. 
# Quando um professor precisa instalar uma biblioteca para
# usar em sua disciplina (ex: Pacote A), o sistema de gerenciamento do laboratório precisa
# baixar automaticamente as dependências dela (ex: Pacote B e Pacote C). 
# O problema é que,devido à falta de padronização nos pedidos recentes, acabaram surgindo dependências
# circulares (O Pacote A exige o B, que exige o C, que por sua vez exige o A). 
# Ao tentar instalar isso, o gerenciador entra num loop infinito e trava o servidor do NRC.
# Implemente um algoritmo utilizando Busca em Profundidade (DFS) com a estratégia das 3
# Cores (Branco, Cinza e Preto) para verificar a integridade de um repositório.

# Entrada: Um grafo direcionado onde os vértices são pacotes de software e as arestas
# representam dependências (A→ B significa "A depende de B").

# Saída Esperada: O programa deve imprimir [INSTALAÇÃO LIBERADA] se o grafo for um
# DAG (Direcionado Acíclico), ou [ERRO: DEPENDÊNCIA CIRCULAR DETECTADA]
# caso o algoritmo esbarre em um vértice "Cinza" durante a recursão

BRANCO = 0
CINZA  = 1
PRETO  = 2

def dfs(vertice, grafo, cor):
    cor[vertice] = CINZA

    for vizinho in grafo[vertice]:
        if cor[vizinho] == CINZA:
            return True
        if cor[vizinho] == BRANCO:
            if dfs(vizinho, grafo, cor):
                return True

    cor[vertice] = PRETO
    return False

def verificar_repositorio(grafo):
    cor = {}
    for v in grafo:
        cor[v] = BRANCO

    for vertice in grafo:
        if cor[vertice] == BRANCO:
            if dfs(vertice, grafo, cor):
                print("[ERRO: DEPENDÊNCIA CIRCULAR DETECTADA]")
                return

    print("[INSTALAÇÃO LIBERADA]")


# Grafo SEM ciclo: A->B->C
grafo_dag = {
    "A": ["B"],
    "B": ["C"],
    "C": [],
}

# Grafo COM ciclo: A->B->C->A
grafo_ciclico = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"],
}

print("\nTeste 1 DAG (Direcionado Acíclico):")
verificar_repositorio(grafo_dag)

print("\nTeste 2 (Ciclo A->B->C->A):")
verificar_repositorio(grafo_ciclico)