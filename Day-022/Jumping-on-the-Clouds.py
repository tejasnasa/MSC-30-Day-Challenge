import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    jumps = 0
    
    for i in c:
        if (i == 1):
            jumps += 1
    jumps = len(c) - jumps - 1
    
    i = 0
    
    while (i < len(c) - 2):
        if (c[i] == 0 and c[i + 1] == 0 and c[i + 2] == 0):
            jumps -= 1
            i += 2
        else:
            i += 1
    
    return jumps
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
