import math
import os
import random
import re
import sys

def permutationEquation(p):
    ans = []
    
    for num in range(1, max(p)+1):
        ans.append(p.index(p.index(num)+1)+1)
        
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
