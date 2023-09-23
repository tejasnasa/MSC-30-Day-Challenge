import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    i = 0
    result = [0, 0]
    while (i < 3):
        if (a[i] > b[i]):
            result[0] += 1
        if (a[i] < b[i]):
            result[1] += 1
        i += 1
    
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
