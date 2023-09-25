import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    summ = 0
    x = 5
    for i in range (0, n):
        for j in range (i + 1, n):
            if (ar[i] == ar[j]):
                summ += 1
                x += 2
                ar[i] = x ** 2 - 1
                ar[j] = x ** 2 + 1
                
            
    return summ

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
