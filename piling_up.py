from random import randint
def checker(arr) :
    for i in range(len(arr)) :
        if arr[i] >= arr[i+1] :
            return True

        else :
            return False 


def func() :
    choice = randint(-1,0)

    testcase = int(input())
    for each in range(testcase) :
        num_cubes = int(input())
        licubes = list(map(int,input().rstrip().split()))
        temp = list()
        high = len(licubes)-1
        low = choice
        for i in licubes :
            
            if licubes[low] >= licubes[high] :
                temp.append(licubes[low])
                temp.append(licubes[high])
                high -= 1
                low += 1

        if checker(temp) is True :
            print("Yes")
        else : print("No")

if __name__ == "__main__":
    func()