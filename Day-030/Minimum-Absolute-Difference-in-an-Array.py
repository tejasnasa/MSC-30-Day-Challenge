import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(arr):
    arr.sort()
    minn = 10000000000
    for i in range(0, len(arr)-1):
        if (abs(arr[i] - arr[i+1]) < minn):
            minn = abs(arr[i] - arr[i+1])
    return minn

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
