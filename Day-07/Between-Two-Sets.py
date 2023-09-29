import math
import os
import random
import re
import sys

def getTotalX(a, b):
    ans = 0
    
    for i in range (a[len(a) - 1], b[0] + 1):
        ans += (all([i % aa == 0 for aa in a]) and all([bb % i == 0 for bb in b]))
            
    return ans
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
