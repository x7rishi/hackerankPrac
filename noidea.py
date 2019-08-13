#https://www.hackerrank.com/challenges/no-idea/problem
def noidea(n,m):
    integer = list(map(int,input().split()))
    happiness = 0
    tempa = set(map(int,input().split()))
    tempb = set(map(int,input().split()))
    #print(integer)
    #print(tempa)
    #print(tempb)
    g = tempa.intersection(integer)
    h = tempb.intersection(integer)
    happiness = len(g)*1 - len(h)
    return happiness

 

if "__main__" == __name__ :
    x,y = [int(x) for x in input().split()]
    print(noidea(x,y))
