import math
import os
import random
import re
import sys


def minimumDistances(a):
    minn = 100000;
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if(a[i] == a[j] and j - i < minn):
                minn = j - i;
              
    if(minn == 100000):
        return str(-1)
        
    else:
        return str(minn)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()


