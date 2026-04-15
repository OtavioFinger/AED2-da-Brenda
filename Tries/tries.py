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


    def print(self, root = None, height=0): #tipo uma busca por profundidade pre order
        if root is None:
            root = self.root
        
        print(root.value.rjust(height)) # só pra printar
        for key, node in root.filhos.items():
            self.print(node, height + 1)

trie = Trie()
trie.inserir("otavio")
trie.inserir("otario")
trie.print()