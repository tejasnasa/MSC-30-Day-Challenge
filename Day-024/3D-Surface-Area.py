import math
import os
import random
import re
import sys


def surfaceArea(A):
    ans = 2 * len(A) * len(A[0])
    
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):

            if (i == 0):
                ans += A[i][j]
            
            if (j == 0):
                ans += A[i][j]
              
            
            if (j == W - 1):
                ans += A[i][j]
              
            else:
                ans += abs(A[i][j] - A[i][j + 1])
              

            if (i == H - 1):
                ans += A[i][j]
              
            else:
                ans += abs(A[i][j] - A[i + 1][j])
                
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()

