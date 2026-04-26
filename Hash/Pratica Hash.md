
# Tabelas HASH


## Conceito de Hash

É uma estrutura de dados que tem como propósito ter uma busca melhor, mais eficiente.

*Obs: Em uma busca binária, meu tempo de busca é de O(log n). Entretanto, e se pudessemos reduzir este tempo ainda mais?

Essa CHAVE na verdade vai passar por uma FUNÇÃO, obtendo um ÍNDICE para minha Tabela Hash. Sabendo do índice, posso ir buscar em tempo constante O(1) o dado que eu quero, lembrando:

O(log n) mais rápido que O(1)

*Chave Hash:* 
Precisa
*Exemplo: CPF, ID, um elemento que nunca vai se repetir.

*Função Hash/Espalhamento:* 
Vai pegar a chave e transformar em um índice.

*Tabela Hash:*
Comumente é um vetor, esse vetor pode ser de qualquer tipo.

## Probleminhas da Hash

1. Alto consumo de memória, devido a alocação da tabela.