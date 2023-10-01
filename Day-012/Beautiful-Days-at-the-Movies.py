import math
import os
import random
import re
import sys

def beautifulDays(i, j, k):
    x = 0
    
    for i in range(i, j + 1):
        if (abs(i - int(str(i)[::-1])) % k == 0):
            x += 1
            
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
