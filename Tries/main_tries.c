#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define ALFABETO 26

typedef struct NODO {
    struct NODO *filhos[ALFABETO];
    char letrinha;
    bool existe;
} NODO; //NODO agora é um tipo

NODO* Criar_Nodo();
void Inserir_Palavra( NODO *raiz, char *palavra );

int main() {


    return 0;
}

NODO* Criar_Nodo() { //new_node é um ponteiro que aponta pro new node

    NODO *new_nodo = NULL;

    NODO *new_nodo = (NODO*)malloc(sizeof(NODO));

    if (new_nodo->existe) {

        new_nodo->existe = false;

        for ( int i = 0; i <= ALFABETO; i++ ) {
            new_nodo->filhos[i] = NULL;
        }
    }

    return new_nodo;

}

void Inserir_Palavra( NODO *raiz, char *palavra ) {

    //vamos criar um ponteiro para percorrer
    NODO *atual = raiz;

    int tamanho_palavra = strlen(palavra);
    

    for ( int i = 0; i < tamanho_palavra; i++ ) {

        int indice = palavra[i] - 'a'; // a é 0, b é 1

        if ( atual->filhos[indice] == NULL ) { // se não tiver o nodo daquela letra, crie-o
            Criar_Nodo();
        } 

        atual = atual->filhos[indice]; // se tiver, pode seguir
    }

    atual->existe = true; // depois do loop, marca fim de palavra

}

// Implemente uma função buscar_palavra que retorne True se a palavra estiver na trie e False caso contrário.