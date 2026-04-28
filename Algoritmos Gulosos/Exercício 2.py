
#  Dado um intervalo [0, L] e um conjunto de subintervalos, s
# elecione o menor número de intervalos que cubram completamente [0, L], se possível.
#  Entrada:

l = 10
intervalos = [(0,3), (2,5), (4,7), (6,10), (8,10)]

def exercicio2(l, intervalos):

    intervalos.sort()

    atual = 0
    i = 0
    resposta = []
    tam_intervalos = len(intervalos)

    while atual < l:

        melhor_fim = atual
        melhor_intervalo = None

        while i < tam_intervalos and intervalos[i][0] <= atual:

            if intervalos[i][1] > melhor_fim:
                melhor_fim = intervalos[i][1]
                melhor_intervalo = intervalos[i]

            i += 1


        if melhor_intervalo is None:
            return None

        resposta.append(melhor_intervalo)
        atual = melhor_fim # atualiza o novo ponto

    return resposta

print(exercicio2( l, intervalos))