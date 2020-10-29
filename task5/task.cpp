//Para comipilar:
//g++ -o pratica5 -O3 -std=c++11 pratica5.cpp -pthread -lm
//icpc -o pratica5 -O3 -std=c++11 pratica5.cpp -pthread -lm


#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <thread>
#include <math.h>
#include <sys/time.h>
#include <time.h>
#include <vector>

using namespace std;

// Imprime uma mensagem de erro e encerra o programa com o código da falha
#define DIE(...) { \
        fprintf(stderr, __VA_ARGS__); \
        exit(EXIT_FAILURE); \
}

typedef long long ll;

unsigned numThreads;
ll numElementos;
double *V;

double MyClock() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (tv.tv_sec * 1000000) + tv.tv_usec;
}

// Função fatorial. 
ll fatorial(int n) {
        ll f = 1;
        for (int i = 2; i <= n; ++i)
            f *= i;
        return f;
}

// Função custosa e sem sentido
double funcaoTrabalhosa(double x) {
        double a = atan(x) + cos(x);
        double dadx = (1./(pow(x+0.2, 2) + 1.)) - sin(x);
        double k = a + (dadx * pow(x, 12)) / (double)fatorial(9);
        double s = 12.12 / (double)fatorial(12) / fatorial(11);
        k += (pow(x, 5) / (double)fatorial(12)) * s;
        k -= sin(dadx) + 2 * M_PI * cos(dadx);
        return k > 0 ? k : -k;
}

void preencheVetor(int ini, int fim){
    //Preenche o valor
    for(ll i=ini; i<=fim; i++){
        V[i] = funcaoTrabalhosa(i);
    }
    //Na posição central, é colocado um valor negativo
    V[numElementos/2] = -1;
}
                                                                             
int main(int argc, char *argv[]) {
    double inicio = MyClock();
    int begin, end, i;

    // Valida os argumentos
    if (argc != 3 || sscanf(argv[1], "%u", &numThreads) != 1 || sscanf(argv[2], "%lld", &numElementos) != 1) {
        printf("usage: %s <numThreads> <numElementos>\n", argv[0]);
        return 1;
    }

    if (numElementos < 0)
        DIE("Tamanho do vetor invalido\n");

    vector<thread> threads(numThreads);

    srand(0);

    if((V = (double *)malloc(numElementos * sizeof(double))) == NULL)
        DIE("Erro na alocação do vetor V\n");

    
    // Você deve paraleliazar apenas essa função
    begin=1;
    end = numElementos/numThreads;
            // printf("%d \n", end);

    for (i = 0; i < numThreads; i++)
    {

        numThreads-1 == i ? threads[i] = thread(preencheVetor, begin, end) :
        threads[i] = thread(preencheVetor, begin, end);
        begin = end+1;
        end += numElementos/numThreads;       
    }

    for (int i = 0; i < numThreads; i++)
    {
        threads[i].join();
    }
    
    
    

    printf("%.5lf\n", (MyClock()-inicio)/CLOCKS_PER_SEC); //segundos
    free(V);

	return 0;
}