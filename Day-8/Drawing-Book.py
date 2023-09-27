import math
import os
import random
import re
import sys

def pageCount(n, p):
    if (p // 2 < n // 2 - p // 2):
        return p // 2
    else:
        return n // 2 - p // 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
