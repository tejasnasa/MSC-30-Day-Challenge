import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    kaps = []
  
    for i in range(p, q + 1):
        s = str(i**2)
        right = s[len(s)//2:]
        left = '0' if s[:len(s)//2] == '' else s[:len(s)//2]
        if (int(left) + int(right) == i):
            kaps.append(i)
        
    if len(kaps) == 0:
        print("INVALID RANGE")
      
    else:
        print(" ".join(str(x) for x in kaps))

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)


