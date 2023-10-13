import math
import os
import random
import re
import sys


def larrysArray(A):
    for i in range(0, len(A)):
        for j in range(1, len(A) - 1):
            a, b, c = A[j - 1], A[j], A[j + 1]
          
            if (a > b or c < a):
                A[j - 1], A[j], A[j + 1] = A[j], A[j + 1], A[j - 1]
        
    if (A == sorted(A)):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()




