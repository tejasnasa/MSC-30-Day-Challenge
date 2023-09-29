import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    billsum = 0
    for i in range (0, len(bill)):
        if (i != k):
            billsum += bill[i]
    
    if (billsum / 2 == b):
        print ("Bon Appetit")
    
    else:
        print (int(bill[k] / 2))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
