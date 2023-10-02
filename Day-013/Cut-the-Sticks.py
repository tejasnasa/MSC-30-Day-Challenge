import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    x = []
    while (len(arr) > 0):
        x.append(len(arr))
        m = min(arr)
        while m in arr:
            arr.remove(min(arr))
        for i in arr:
            i -= min(arr)
        
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
