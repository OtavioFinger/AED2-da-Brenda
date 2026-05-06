# Árvores B (B-Tree)

## Introdução

Surgem para resolver problemas envolvendo busca. Se dá como uma árvore vetor, que contém espaços para armazenar valores mas também chaves que levam para níveis abaixo da árvore. Seu objetivo é reduzir altura.

Ordem da Árvore: 
- Número mínimo de elementos que uma página deve ter.
- Número máximo de filhos que uma página pode ter.

## Regras da Árvore B

1. Cada página, EXCETO a raíz, deve ter pelo menos 50% de ocupação (considerando a Ordem da Árvore).

*Obs: Ímpar é melhor, pq o número de chaves será par*

2. Número de filhos (exceto folha) deve ser o número de chaves preenchidas no momento + 1. 

3. Todas as folhas estão no mesmo nível (o crescimento é para cima)