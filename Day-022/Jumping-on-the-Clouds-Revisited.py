import math
import os
import random
import re
import sys

def jumpingOnClouds(c, k):
    x = k % n
    energy = 99 - c[x]*2
    
    while (x != 0):
        x = (x + k) % n
        energy -= 1 + c[x]*2
        
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
