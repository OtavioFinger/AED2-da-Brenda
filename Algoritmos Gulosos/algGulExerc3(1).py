def ordenar_por_lucro(tarefas):
    return sorted(tarefas, key=pegar_lucro, reverse=True)


def pegar_lucro(tarefa):
    return tarefa['lucro']


def encontrar_maior_prazo(tarefas):
    maior = tarefas[0]['prazo']
    
    for tarefa in tarefas:
        if tarefa['prazo'] > maior:
            maior = tarefa['prazo']
    
    return maior


def organizar_agenda(tarefas):
    tarefas_ordenadas = ordenar_por_lucro(tarefas)

    max_prazo = encontrar_maior_prazo(tarefas)

    agenda = [None] * (max_prazo + 1)

    lucro_total = 0
    for tarefa in tarefas_ordenadas:
        prazo = tarefa['prazo']
        lucro = tarefa['lucro']
        identificador = tarefa['id']

        for dia in range(prazo, 0, -1):
            if agenda[dia] is None:
                agenda[dia] = identificador
                lucro_total += lucro
                break

    agenda_final = []

    for dia in range(1, max_prazo + 1):
        if agenda[dia] is not None:
            texto = "Dia " + str(dia) + ": " + agenda[dia]
        else:
            texto = "Dia " + str(dia) + ": Livre"

        agenda_final.append(texto)

    return agenda_final, lucro_total


# ================= TESTE =================

tarefas = [
    {'id': 'A', 'prazo': 2, 'lucro': 100},
    {'id': 'B', 'prazo': 1, 'lucro': 19},
    {'id': 'C', 'prazo': 2, 'lucro': 27},
    {'id': 'D', 'prazo': 1, 'lucro': 25},
    {'id': 'E', 'prazo': 3, 'lucro': 15}
]

agenda, lucro_total = organizar_agenda(tarefas)

print("Agenda:")
for item in agenda:
    print(item)

print("-" * 26)
print("Lucro:", lucro_total)

# Qual a escolha gulosa: A escolha gulosa nesse algoritmo busca achar e selecionar a tarefa com maior lucro e a colocar no ultimo dia possivel antes de seu prazo expirar
# Por que essa escolha não compromete a solução ótima: Pois ela prioriza as tarefas com maior lucro, ou seja, se é possivel alocar a tarefa com maior lucro, essa sera alocada. Além disso, o algoritmo busca alocar as tarefas o mais tarde possível, fazendo com que as chances de encaixar a tarefa sejam maior.