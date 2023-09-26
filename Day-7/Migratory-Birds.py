import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    count = [0] * 6
    
    for bird in arr:
        count[bird] += 1
    
    return count.index(max(count))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
