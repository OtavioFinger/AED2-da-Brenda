
# Tabelas HASH

## Conceito de Hash

É uma estrutura de dados que tem como propósito ter uma busca melhor, mais eficiente.

*Obs: Em uma busca binária, meu tempo de busca é de O(log n). Entretanto, e se pudessemos reduzir este tempo ainda mais?

Essa CHAVE na verdade vai passar por uma FUNÇÃO, obtendo um ÍNDICE para minha Tabela Hash. Sabendo do índice, posso ir buscar em tempo constante O(1) o dado que eu quero, lembrando:

*Obs: O(log n) normalmente mais lento que O(1)*

**Chave Hash:** 
Precisa
*Exemplo: CPF, ID, um elemento que nunca vai se repetir.

**Função Hash/Espalhamento:** 
Vai pegar a chave e transformar em um índice.

**Tabela Hash:**
Comumente é um vetor, esse vetor pode ser de qualquer tipo.

## Probleminhas da Hash

COMUMENTE, essas funções podem gerar o mesmo índice a partir de chaves diferentes, gerando uma COLISÃO. Por isso, você como programador tem duas opções:

1. Fazer uma função de espalhamento melhor, que permita colocar em diferentes índices.
1.1 Uma estratégia sobre isso é criar uma tabela de tamanho primo. Pois quando fizer uma função que use resto(%), ela terá menos colisões.

**TAMANHO: M = 2 * (tamanho do meu conjunto de dados) e pegue o primo mais próximo.**

**Fator de Carga: fc = (tamanho do meu conjunto de dados)/(TAMANHO)

2. Implementar um sistela de lista a partir de um índice. Assim, 