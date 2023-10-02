import math
import os
import random
import re
import sys

def repeatedString(s, n):
    x = n // len(s)
    y = n % len(s)
    count = s[:y].count('a') * (x + 1) + s[y:].count('a') * x
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
