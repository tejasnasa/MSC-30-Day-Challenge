import math
import os
import random
import re
import sys


def extraLongFactorials(n):
    val = 1
    while (n != 1):
        val *= n
        n -= 1
    print(val)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
