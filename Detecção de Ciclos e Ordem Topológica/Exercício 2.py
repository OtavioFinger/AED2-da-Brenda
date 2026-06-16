# Exercício 2*. Os colegiados dos cursos de Computação precisam de um sistema que ajude os
# calouros a montarem os seus horários de matrícula. O sistema recebe a grade curricular
# completa com os pré-requisitos de cada disciplina. No entanto, os alunos frequentemente têm
# dificuldades em interpretar o Projeto Pedagógico do Curso (PPC) e não sabem qual disciplina
# devem priorizar primeiro para não "trancarem" a sua grade no futuro.

BRANCO = 0
CINZA  = 1
PRETO  = 2

grafo = {
    "Programação de Computadores": ["AED I"],
    "AED I":                       ["AED II", "POO", "Grafos"],
    "AED II":                      [],
    "POO":                         [],
    "Grafos":                      [],
}

pilha = []

cor = {}
for v in grafo:
    cor[v] = BRANCO

def dfs(vertice):
    cor[vertice] = CINZA

    for vizinho in grafo[vertice]:
        if cor[vizinho] == BRANCO:
            dfs(vizinho)

    cor[vertice] = PRETO
    pilha.append(vertice)

for vertice in grafo:
    if cor[vertice] == BRANCO:
        dfs(vertice)

pilha.reverse()

print("Trilha de Estudos sugerida:")
for i in range(len(pilha)):
    print(str(i + 1) + ". " + pilha[i])

# Acha a disciplina com mais saídas
critica = ""
maior = 0
for v in grafo:
    if len(grafo[v]) > maior:
        maior = len(grafo[v])
        critica = v

print("\n[ALERTA] A disciplina mais crítica do currículo é \"" + critica + "\", pois ela é pré-requisito direto para " + str(maior) + " outras disciplinas.")