import math
import os
import random
import re
import sys

def twoStrings(s1, s2):
    s3 = set(s1) & set(s2)
    if (len(s3) > 0):
        return "YES"
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
