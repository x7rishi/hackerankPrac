# n = int(input())
# word = list()
# for _ in range(n) :
#     word.append(input().rstrip())

# counter = list()
# distinctword = list(set((word)))
# print(len(distinctword))
# k = 0 
# for i,j in zip(word,distinctword) :
#     counter.append(word.count(i))
#     k += 0 
#     print(counter[k],end = " ")

# for i in range(len(distinctword)) :
#     counter.append(word.count(word[i]))
#     print(counter[i])



n = int(input())
word = list()
for _ in range(n) :
    word.append(input().rstrip())

counter = list()
distinctword = list(dict.fromkeys(word))
print(len(distinctword))

for i in range(len(distinctword)) :
    # counter.append(word.count(word[i]))
    print(word.count(word[i]) , end = " ")

