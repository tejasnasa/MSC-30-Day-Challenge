import math
import os
import random
import re
import sys

def plusMinus(arr):
    le = len(arr)
    i = 0
    p = 0
    n = 0
    z = 0
    while (i < le):
        if (arr[i] > 0):
            p += 1
        elif (arr[i] < 0):
            n += 1
        else:
            z += 1
        i += 1
    
    print((p/le), "\n", (n/le), "\n", (z/le))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
