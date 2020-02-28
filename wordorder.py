# n = int(input())
# word = list()
# for _ in range(n) :
#     word.append(input().rstrip())

def counter(arr) :
    # count = 0 
    # length = len(arr)
    counter = list()
    for i,j in zip(arr,distinctword) :
        counter.append(arr.count(i))
    

    for i in counter :
        print(i, end = " ")

def removeduplicate(arr):
    templist = []
    for i in arr :
        if i not in templist :
            templist.append(i)
    
    return templist
n = 4
word = ['bcdef', 'abcdefg', 'bcde', 'bcdef']


distinctword = removeduplicate(word)

print(len(distinctword))
print(counter(word))


    # return counter

# bcdef
# abcdefg
# bcde
# bcdef

# ["bcdef",
# "abcdefg",
# "bcde",
# "bcdef"]

