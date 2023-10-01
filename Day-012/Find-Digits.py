import math
import os
import random
import re
import sys

def findDigits(n):
    x = 0
    for i in str(n):
        if (i != '0' and n % int(i) == 0):
            x += 1
            
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
