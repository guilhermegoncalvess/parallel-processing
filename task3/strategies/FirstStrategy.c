#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>

double MyClock() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (tv.tv_sec * 1000000) + tv.tv_usec;
}

void firstStrategy( int** A, int** B, int** C, int n )
{
  int i, j, k, l;

  for( i=0; i < n; i++)
  {
    for ( j = 0;  j < n;  j++ )
    {
      int sum = 0;
      for ( k = 0; k < n; k++)
      {
        sum += A[i][k] * B[k][i];
      }
      
      C[i][j] = sum;
    }
  }
}

int main(int argc, char *argv[]){                    
    if (argc != 2) {
		fprintf(stderr, "usage: prog <N>\n");
		exit(1);
    }
    int N = atoi(argv[1]);
    /* Cria a matriz */
    // Se tiverem problemas com a declaração estática, mude para a dinâmica 
    int **A= (int**)malloc( N*sizeof(int*)); 
    int **B= (int**)malloc( N*sizeof(int*)); 
    int **C = (int**)malloc( N*sizeof(int*));
    int i;
    /* Inicializa a matriz */
    for( i=0; i<N; ++i)
    {
      A[i] = (int*)malloc( N*sizeof(int));
      B[i] = (int*)malloc( N*sizeof(int));
      C[i] = (int*)malloc( N*sizeof(int));
    }
    for(int i=0; i<N; ++i)
    {
    	for(int j=0; j<N; ++j)
      {
    		A[i][j] = 1;
        B[i][j] = 1;
        C[i][j] = 0;
    	}
    }
    double inicio = MyClock();
    /* Calcula o valor de C = AxB                              */
    /* Implemente a multiplicação das matrizes A e B abaixo    */
    /* se prefirir, pode fazer uma função para fazer o calculo */

    firstStrategy(A, B, C, N);
    printf("%.15lf\n", (MyClock()-inicio)/CLOCKS_PER_SEC);

    // secondStrategy(A, B, C, N);
    // printf("%.15lf\n", (MyClock()-inicio)/CLOCKS_PER_SEC);

    // thirdStrategy(A, B, C, N);
    // printf("%.15lf\n", (MyClock()-inicio)/CLOCKS_PER_SEC);

    // fourthStrategy(A, B, C, N);
    // printf("%.15lf\n", (MyClock()-inicio)/CLOCKS_PER_SEC);

    // fifthStrategy(A, B, C, N);
    // printf("%.15lf\n", (MyClock()-inicio)/CLOCKS_PER_SEC);

    // sixthStrategy(A, B, C, N);
    // printf("%.15lf\n", (MyClock()-inicio)/CLOCKS_PER_SEC);

    return 0;
}