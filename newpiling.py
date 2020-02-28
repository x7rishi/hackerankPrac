import random

arr = [0]*5

choice = random.randint(-1,0)
# it choice either from left or right 

def checker(arr) :
    if len(arr)  == 1 :
        return False 
    else :

        for i in range(len(arr)) :
            if arr[i] >= arr[i+1] :
                return True

            else :
                return False 


testcase = int(input())
for each in range(testcase) :
    num_of_cubes = int(input())
    list_of_cubes = list(map(int,input().rstrip().split()))
    high = len(list_of_cubes) - 1
    low = 0 # 0 or last element
    i = 0 
    print(list_of_cubes)
    temp = list()
    while (i < len(list_of_cubes)) : # traverse each elem of the list of cubes
        if list_of_cubes[0] >= list_of_cubes[high] :
            temp.append(list_of_cubes[high])


            high = len(list_of_cubes) - 1
        else :
            temp.append(list_of_cubes[low])
            
        i+= 1 
        # else :
        #     break 
    print(temp)
    if checker(temp) == True :
        print("Yes")
    else : print("No")