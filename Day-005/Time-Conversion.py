import math
import os
import random
import re
import sys

def timeConversion(s):
    if (s[8] == "P" and int(s[0:2]) != 12):
        mil = str(int(s[0:2]) + 12)
    elif (s[8] == "A" and s[0:2] == "12"):
        mil = ("00")
    else:
        mil = s[0:2]
    mil += s[2:8]
    return mil

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
