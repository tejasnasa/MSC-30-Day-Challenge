import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    i = 0
    lrsum = 0
    rlsum = 0
    
    while (i < len(arr)):
        lrsum += arr[i][i]
        rlsum += arr[len(arr) - i - 1][i]
        i += 1
    
    return abs(lrsum - rlsum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
