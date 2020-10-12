#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>

double MyClock() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (tv.tv_sec * 1000) + tv.tv_usec;
}

int sumElements(int **matrix, int n){
    int i,j;
    int sum= 0;

    for (i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            sum+= matrix[i][j];
        }
    }
	
	printf("%d", sum);
    return sum;
}

int main(int argc, char *argv[]){                    
    if (argc != 2) {
		fprintf(stderr, "Uso: nomePrograma <N>\n");
		exit(1);
    }
    int N = atoi(argv[1]);

    int i,j;

    int **matrix;

    matrix = (int**)malloc(N*sizeof(int*));
	for(i=0; i<N;i++)
    {
		matrix[i]= (int*)malloc(N*sizeof(int));
		for(j=0; j<N; j++)
            matrix[i][j] = 1;
		
	}

    double inicio = MyClock();
        int sum = sumElements(matrix, N);
        printf("%.10lf\n", (MyClock()-inicio)/CLOCKS_PER_SEC);

    return 0;
}
