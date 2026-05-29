# Uma montadora de veículos possui duas linhas de montagem concorrentes, cada uma
# com n estações de trabalho. O tempo para passar por cada estação varia, e existe um
# custo de tempo adicional se o chassi do carro precisar trocar da Linha 1 para a Linha 2
# no meio do processo (e vice-versa). Com base no modelo matemático deixado como
# tarefa na última aula teórica, implemente um algoritmo em Programação Dinâmica
# que calcule o tempo mínimo total para um carro sair da fábrica. O código deve
# declarar os vetores de custo de entrada (e), saída (x), tempo nas estações (a) e tempo
# de transição (t) com os mesmos valores do exemplo. (Nota: não é preciso considerar a
# a reconstrução do caminho, calcule apenas o custo mínimo)

# Número de estações
n = 6

# Tempo nas estações (linha 1 e linha 2)
                # Muda-se aqui:
a = [ [5, 8, 4, 6, 7, 3], [6, 4, 7, 3, 6, 8] ]   # linha 1 e 2
 
# Tempo de transferência (de linha 1 pra 2, e de linha 2 pra 1)
# t[i][j] = custo de sair da linha i após estação j
                # Muda-se aqui:
t = [ [3, 2, 4, 1, 3], [1, 3, 2, 3, 2] ]  # linha 1 -> linha 2 e linha 2 -> linha 1
 
# Tempo de entrada
                # Muda-se aqui:
e = [3, 2]  # e1, e2
 
# Tempo de saída
                # Muda-se aqui:
x = [2, 4]  # x1, x2


# Vetores para guardar os tempos mínimos
f1 = [0] * n
f2 = [0] * n

# Casos base: primeira estação
f1[0] = e[0] + a[0][0]
f2[0] = e[1] + a[1][0]

# Preenche os demais usando a recorrência dos slides
for j in range(1, n):
    f1[j] = min(f1[j-1] + a[0][j], f2[j-1] + t[1][j-1] + a[0][j])
    f2[j] = min(f2[j-1] + a[1][j], f1[j-1] + t[0][j-1] + a[1][j])

# Resultado final: mínimo entre sair pela linha 1 ou linha 2
f_valorotimo = min(f1[n-1] + x[0], f2[n-1] + x[1])

print("Tempos mínimos acumulados - Linha 1:", f1)
print("Tempos mínimos acumulados - Linha 2:", f2)
print("\nTempo mínimo total:", f_valorotimo)