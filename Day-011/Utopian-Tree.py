import math
import os
import random
import re
import sys

def utopianTree(n):
    h = 1
    if (n % 2 == 0):
        for i in range(0, int(n / 2)):
            h = 2 * h + 1
        return h
    
    else:
        for i in range(0, int((n - 1)/ 2)):
            h = 2 * h + 1
        return 2 * h

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
