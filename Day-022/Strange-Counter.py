import math
import os
import random
import re
import sys

def strangeCounter(t):
    initial = 3
    cycleTime = 3

    while (t > cycleTime):
        initial *= 2
        cycleTime += initial

    return cycleTime - t + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
