#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    
    int n;
    scanf("%i", &n);
    int ARR[n];
    int sum = 0;
    
    for (int i = 0; i < n; i++)
    {
        scanf("%i", &ARR[n]);
        sum += ARR[n];
    }    
    
    printf("%i", sum);
        
    return 0;
}
