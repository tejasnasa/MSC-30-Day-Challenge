import math
import os
import random
import re
import sys

def encryption(s):
    columns = int(math.ceil(len(s) ** 0.5))
    ans = ("")
    
    for i in range(0, columns):
        k = i
        for j in range(k, len(s), columns):
            ans += s[j]
        ans += (" ")
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
