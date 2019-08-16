#https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen&isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    n = len(arr)
    positive = negative = zero = 0.000000
    for i in arr:
        if i> 0 :
            positive +=1
        elif i<0 :
            negative += 1
        else :
            zero +=1
    fracposi = positive/n
    fracnegi = negative/n
    fraczero = zero/n
    print("%1.6f\n%1.6f\n%1.6f"%(fracposi,fracnegi,fraczero),end= "")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
