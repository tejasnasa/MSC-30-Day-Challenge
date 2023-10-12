import math
import os
import random
import re
import sys


def chocolateFeast(n, c, m):
    ans = int(n / c)
    if ans >= m:
        x = ans
        while x > 0:
            x = x - m
            if x >= 0:
                ans += 1
                x += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
