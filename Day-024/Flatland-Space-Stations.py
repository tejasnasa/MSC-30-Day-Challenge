import math
import os
import random
import re
import sys


def flatlandSpaceStations(n, c):
    c = sorted(c)
    ans = c[0]
    
    for i in range(1, len(c)):
        ans = max(ans, (c[i] - c[i - 1]) // 2)
        
    ans = max(ans, n - 1 - c[-1])
        
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
