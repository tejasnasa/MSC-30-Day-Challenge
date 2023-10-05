import math
import os
import random
import re
import sys

def beautifulTriplets(d, arr):
    ans = 0
    for i in arr:
        if i + d in arr and i + d * 2 in arr:
            ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
