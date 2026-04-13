# 1. A partir de uma uma implementação funcional de uma Trie padrão (ou uma de suas variantes, como TST ou Radix Tree), sua tarefa é expandir a #funcionalidade da estrutura.
# Arthur Trettin Bast e Otávio Finger

def inserir_trie(trie, palavra):
    curr = trie
    
    for char in palavra:
        if char not in curr:
            curr[char] = {}
        
        curr = curr[char]
        
    curr['final'] = True
    
def achar_palavra(node, prefixo, resultado):
    if node.get('final'):
        resultado.append(prefixo)
    
    for char, prox_node in node.items():
        if char != 'final':
            achar_palavra(prox_node, prefixo + char, resultado)
            
    
    
    
def buscar_por_prefixo(trie, prefixo):
    
    curr = trie
    
    for char in prefixo:
        if char not in curr:
            return []
        
        curr = curr[char]
        
    resultado = []
    
    achar_palavra(curr, prefixo, resultado)
    
    return resultado
    
nova_trie = {}
inserir_trie(nova_trie, 'mar')
inserir_trie(nova_trie, 'maré')
inserir_trie(nova_trie, 'martelo')
inserir_trie(nova_trie, 'memoria')
inserir_trie(nova_trie, 'mercadoria')

print(buscar_por_prefixo(nova_trie, 'mar'))