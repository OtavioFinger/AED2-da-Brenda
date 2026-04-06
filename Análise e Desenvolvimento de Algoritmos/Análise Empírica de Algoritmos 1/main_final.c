#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// As linguagens modernas nos oferecem estruturas convenientes como ArrayList (Java), vector (C++) ou 
// list (Python) que crescem magicamente à medida que inserimos elementos. 
// Neste exercício, você deverá implementar o seu próprio vetor dinâmico do zero, utilizando apenas 
// alocação básica de memória (arrays estáticos primitivos).

typedef struct {
    int *dados;
    int tamanho;    
    int capacidade; 
} vetor_dinamico;

long contador_copias = 0;

vetor_dinamico* criar_vetor();
void Inserir(vetor_dinamico *v, int elemento, char estrategia);
void Script(char estrategia, char* nome_estrategia);

int main() {
    
    srand(time(NULL)); //serve pra add elementos aleatorios dps
    Script('A', "Linear");
    Script('B', "Exponencial");

    return 0;
}

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

        // Estratégia A (Crescimento Linear):
        if ( estrategia == 'A' ) {
            nova_capacidade = v->capacidade + 100;
        } 
        // Estratégia B (Crescimento Exponencial):
        else if ( estrategia == 'B' ) {
            nova_capacidade = v->capacidade * 2;
        } else {
            printf("Letra incorreta. Digite somente A ou B");
            free(v->dados);
            free(v);
            exit(1);
           
        }

        //aloca novo array
        int *novo_array = (int*) malloc(nova_capacidade * sizeof(int));

        if ( !novo_array ) {
            printf("Erro de alocação!");
            exit(1);
        }

        //copia elementos do primeiro vetor pro segundo(novo)
        for ( int i = 0; i < v->tamanho; i++ ) {
            novo_array[i] = v->dados[i]; //elemento pra elemento
            contador_copias++; 
        }

        free(v->dados);
        v->dados = novo_array; //ponteiro de dados recebe o novo_array
        v->capacidade = nova_capacidade;
    }

    v->dados[v->tamanho] = elemento; //cada indice do tamanho em novo_array recebe o novo elemento
    v->tamanho++; //aumenta o tamanho (até a capacidade)
}

//Faça um script de teste que insira 10.000 elementos sequencialmente em ambos os vetores. 
//Adicione um contador global para registrar quantas operações de cópia de elementos 
//(do array antigo para o novo) ocorreram no total.

void Script(char estrategia, char* nome_estrategia) {

    contador_copias = 0; 
    vetor_dinamico *v = criar_vetor();

    for ( int i = 0; i < 10000; i++ ) {
        int aleatorio = rand();
        Inserir(v, aleatorio, estrategia);
    }

    printf("Estrategia %s: %ld copias realizadas.\n", nome_estrategia, contador_copias);
    
    free(v->dados);
    free(v);
}

