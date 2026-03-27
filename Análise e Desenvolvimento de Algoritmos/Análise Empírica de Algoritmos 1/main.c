#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    int *dados;
    int tamanho;    
    int capacidade; 
} vetor_dinamico;

long contador_copias = 0;

//Crie uma classe/estrutura VetorDinamico que armazene números inteiros. 
//Ela deve ter uma capacidade inicial de 1 elemento.

vetor_dinamico* criar_vetor() {

    vetor_dinamico *v = (vetor_dinamico*) malloc(sizeof(vetor_dinamico));
    v->capacidade = 1;
    v->tamanho = 0;
    v->dados = (int*) malloc(v->capacidade * sizeof(int));
    return v;
}

//Implemente o método inserir(elemento). Quando o vetor estiver cheio, aloque um novo array, 
//copie todos os elementos antigos para o novo e, em seguida, inserir o novo elemento.

void Inserir(vetor_dinamico *v, int elemento, char estrategia) {

    if ( v->tamanho == v->capacidade ) {
        int nova_capacidade;

        //Estratégia A (Crescimento Linear):
        if ( estrategia == 'A' ) {
            nova_capacidade = v->capacidade + 100;
        } 
        // Estratégia B (Crescimento Exponencial):
        else if ( estrategia == 'B' ) {
            nova_capacidade = v->capacidade * 2;
        }

        int *novo_array = (int*) malloc(nova_capacidade * sizeof(int));

        for ( int i = 0; i < v->tamanho; i++ ) {
            novo_array[i] = v->dados[i];
            contador_copias++; 
        }

        free(v->dados);
        v->dados = novo_array;
        v->capacidade = nova_capacidade;
    }

    v->dados[v->tamanho] = elemento;
    v->tamanho++;
}

//Faça um script de teste que insira 10.000 elementos sequencialmente em ambos os vetores. 
//Adicione um contador global para registrar quantas operações de cópia de elementos 
//(do array antigo para o novo) ocorreram no total.

void Script(char estrategia, char* nome_estrategia) {

    contador_copias = 0; 
    vetor_dinamico *v = criar_vetor();

    for ( int i = 0; i < 10000; i++ ) {
        Inserir(v, i, estrategia);
    }

    printf("Estrategia %s: %ld copias realizadas.\n", nome_estrategia, contador_copias);
    
    free(v->dados);
    free(v);
}

int main() {
    
    Script('A', "Linear");
    Script('B', "Exponencial");

    return 0;
}