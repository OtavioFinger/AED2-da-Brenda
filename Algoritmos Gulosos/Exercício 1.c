#include <stdio.h>
#include <stdlib.h>

// Um carro precisa percorrer uma distância com postos ao longo do caminho. Dado o 
// alcance máximo do carro e a posição dos postos, implemente um algoritmo que minimize o número de paradas.

// distancia_total = 25
// alcance_max = 10
// postos = [5, 10, 15, 20]

#include <stdio.h>

int main() {
    int distancia_total = 25;
    int alcance_max = 10;
    int postos[] = {5, 10, 15, 20};
    int num_postos = 4;
    
    int paradas = 0;
    int posicao_atual = 0;
    int i = 0;
    
    while ( posicao_atual + alcance_max < distancia_total ) {
        int melhor_posto = -1;
        
        // Procura o posto mais distante que AINDA está no alcance
        while ( i < num_postos && (postos[i] <= posicao_atual + alcance_max) ) {
            melhor_posto = postos[i];
            i++;
        }
        
        if ( melhor_posto == -1 ) {
            printf("Não há como chegar ao destino!\n");
            return -1;
        }
        
        posicao_atual = melhor_posto;
        paradas++;
    }
    
    printf("Núnero mínimo de paradas: %d\n", paradas);
    
    return 0;
}