import copy
import math
def diag(arr):
    diag1 = diag2 = 0
    temp = copy.deepcopy(arr)
    for i in temp :
        i.reverse()
    math.
    print("\nYou entered the two-d array element's value \n")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j :
                diag1 += arr[i][i]
                diag2 += temp[i][i]

            print("array[%d][%d] :  %d "%(i,j,arr[i][j]),end = " ",sep= ' ',flush = True)
            
        print("\n")
    #reversing the element of the matrix by row - wise
    print("sum of the diagonal is ",diag1)
    print("sum of the diagonal is ",diag2)
#input of order 4
"""
4
9   13  5   2  
1   11  7   6   
3   7   4   1
6   0   7   10


"""

if __name__ == '__main__' :
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().rstrip().split())))
    diag(arr)
