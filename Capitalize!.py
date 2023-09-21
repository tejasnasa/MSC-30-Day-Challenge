#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function
below.
def solve(s):
  i = 0
  n = len(s.split(" "))
  s1 = ""
  
  while (i < n):
    s1 += (s.split(" ")[i].capitalize() + " ")
    i+= 1
  return s1

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  s = input()
  result = solve(s)
  fptr.write(result + '\n')
  fptr.close()
