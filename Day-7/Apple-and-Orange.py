import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    ac = 0
    bc = 0
    for i in range (len(apples)):
        temp = a + apples[i]
        if (temp in range (s,t + 1)):
            ac += 1
    
    for i in range (len(oranges)):
        temp = b + oranges[i]
        if (temp in range (s, t + 1)):
            bc += 1
    
    print (ac)
    print (bc)
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
