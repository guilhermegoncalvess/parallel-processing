#include <stdio.h>
#include <stdlib.h>


int main(){                    
    
    int i, j, k, divisors=0,sum=0;

    for ( i = 24; i < 10000; ++i)
    {
        for( j = 2; j < i; ++j)
        {
            if( i % j == 0)
            {
                sum = 4;
                for(k = j+1; k < i/j; ++k)
                {
                    if(i % k == 0)
                        sum++;
                }
                if( sum == 8)
                    divisors++;
                sum = 0;
                break;
            }
        }
            
    }
    
    // printf("\n%d", divisors);
    return 0;
}
