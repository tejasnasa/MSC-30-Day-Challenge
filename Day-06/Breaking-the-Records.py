import math
import os
import random
import re
import sys

def breakingRecords(scores):
    maxn = -100
    maxc = 0
    minn = 10000000000
    minc = 0
    
    for i in range (0, len(scores)):
        if (scores[i] > maxn):
            maxn = scores[i]
            maxc += 1
        if (scores[i] < minn):
            minn = scores[i]
            minc += 1
    
    return [maxc - 1, minc - 1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
