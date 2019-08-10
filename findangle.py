# -*- coding: utf-8 -*-
import math
# using law of cosine of triangle

def angle(x,y):
    ab = x
    bc = y
    ac = math.sqrt((ab**2.0 + bc**2.0))
    mc = ac/2
    temp = bc/(mc*2.0)
    angle = math.acos(temp)
    ang= angle*(180/math.pi)
    roundoff = str(round(ang))+'°'
    return roundoff

if "__main__" == __name__:
    ab = float(input())
    bc = float(input())
    print(angle(ab,bc))
