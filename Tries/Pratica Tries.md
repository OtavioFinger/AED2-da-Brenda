
# Introdução

As árvores tries ou R-way trie são um tipo de estrutura de dados em que cada nó dessa árvore pode ter vários filhos, sendo n-ária. A chave para encontrar o dado está implicito na busca, chaves são encontradas a partir do caminho de busca, começando da raíz.

*Chave: É um dado identificador que se usa para encontrar outros dados relacionados. Exemplo: Matrícula do aluno é a chave, usada para encontrar nome, notas e etc.*

Complexidade: 
*O(AK)*
*A = tamanho do alfabeto*
*K = tamanho da chave*
*Também há casos em que se for implementada somente com a inserção de uma letra por vez. Seu custo geral é O(K), representando o tamanho da palavra.*

Resumo: Só compensa se tiver bastante espaço.

## Outros tipos de árvore

Árvore Patricia: Armazena strings ou partes delas, diferentemente das tries que armazenam somente caracteres. 

Radix Tree: Compactar caminhos que tenham apenas um filho, reduzindo o número de nós na árvore. Se eu só tiver G-A-T-O, só vou ter um nodo GATO. Flexibilidade, se eu posso unir informações, eu faço. 
-------
    Principais usos são pra Tabelas de Roteamento de IP, Indexação de Banco de Dados.

*Obs: Patricia e Radix são essencialmente a mesma coisa*

R-Way Tree: mais usado quando alfabeto é pequeno (ex: dígitos 0-9).

TST (Ternary Search Tree): Cada nó tem um caractere e no máximo 3 ponteiros. Tem melhor desempenho quando se trata de espaço. 