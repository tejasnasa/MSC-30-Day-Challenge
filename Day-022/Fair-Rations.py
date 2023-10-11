import math
import os
import random
import re
import sys

def fairRations(B):
    ans = 0

    i = len(B) - 1
    while (i > 0):
        if (B[i] % 2 == 1):
            B[i] += 1
            B[i - 1] += 1
            ans += 2
        i -= 1

    if (B[0] % 2 == 1):
        return ("NO")

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
