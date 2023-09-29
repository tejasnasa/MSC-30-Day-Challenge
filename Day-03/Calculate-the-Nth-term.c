#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int find_nth_term(int n, int a, int b, int c) {
  int L[n];
  L[0] = (char)a;
  L[1] = (char)b;
  L[2] = (char)c;
  
  for (int i = 3; i < n; i++)
  {
      L[i] = (int)L[i-1] + (int)L[i-2] + (int)L[i-3];
  }
  
  return L[n - 1];
}

int main() {
    int n, a, b, c;
  
    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);
 
    printf("%d", ans); 
    return 0;
}
