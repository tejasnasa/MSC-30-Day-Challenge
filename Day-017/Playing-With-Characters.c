#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char a;
    char b[15];
    char c[100];
    
    scanf("%c\n", &a);
    printf("%c\n", a);

    scanf("%s\n", &b);
    printf("%s\n", b);

    scanf("%[^\n]%*c", &c);
    printf("%s\n", c);   
    
    return 0;
}
