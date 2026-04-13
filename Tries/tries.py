# Classe do nodo

class TrieNode:

    #Método Construtor
    def __init__(self, value):
        self.value = value
        self.filhos = {} # 0 .. n filhos
        self.fimDaPalavra = False

    def __str__(self):
        return self.value

# Classe da Trie em si
class Trie:
    #Método Construtor
    def __init__(self):
        self.root = TrieNode("/")
    
#Insere uma palavra na Trie

    def inserir(self,palavra):
        atual = self.root

        for letra in palavra:
            if letra not in atual.filhos:
                atual.filhos[letra] = TrieNode(letra)
            atual = atual.filhos[letra]
        atual.fimDaPalavra = True
