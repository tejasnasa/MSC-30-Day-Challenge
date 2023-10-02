import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    x = 0
    for i in range(0, min(len(s), len(t))):
        if (s[i] == t[i]):
            x += 1
        else:
            break
                
    ans = len(s) - (2 * x) + len(t)
    if (ans == k):
        return "Yes"
    elif (ans < k):
        if (abs(len(s) - len(t)) % 2 == 0):
            return "Yes"
        else:
            if (k % 2 != 0):
                return "Yes"
            else:
                return "No"
    return "No"
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
