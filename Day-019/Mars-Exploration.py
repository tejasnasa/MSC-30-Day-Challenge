import math
import os
import random
import re
import sys

def marsExploration(s):
    ans = 0
    for i in range(int(len(s) / 3)):
        ans += int(s[i * 3] != 'S') + int(s[i * 3 + 1] != 'O') + int(s[i * 3 + 2] != 'S')
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
