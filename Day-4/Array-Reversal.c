#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }
    
    int temp[num];
    for (int i = 0; i < num; i++)
    {
        temp[i] = arr[i];
    }
    
    for (int i = 0; i < num; i++)
    {
        arr[i] = temp[num - i - 1];
    }

    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}
