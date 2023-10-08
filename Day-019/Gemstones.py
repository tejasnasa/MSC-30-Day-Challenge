import math
import os
import random
import re
import sys

def gemstones(arr):
    s = list(set(''.join(arr)))
    
    ans = len(s)
    for c in s:
        for j in arr:
            if c not in j:
                ans -= 1
                break
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
