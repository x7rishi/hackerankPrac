""" string will be AABCAAADA
"""

#https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    n = len(string)
    # printing the  n/k  line where each line i contains string ui.
    tmp = list()
    alphalist=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', \
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', \
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for i in range(n):
        if i%k == 0:
            tmp.append(string[i:i+k])
    print(tmp)
    # tmp =  ['AAB', 'CAA', 'ADA']
    newlist = list()
    
    for ch in tmp :
        
        newlist.append(list(ch))
    print(newlist)
    newlist = [['A', 'A', 'B'], ['C', 'A', 'A'], ['A', 'D', 'A']]
    #for i in newlist :
     #   print("".join(list(set(i)))




    """
    templist = list()
    for i in newlist :
        for j in range(len(i)):
            key = i[j]
            for k in range(1,len(i)) :
                print("key is ",key)
                print (i[k])
                
                break
                #if key == i[k] :
                    
                    #print("Value is k ",k,"and value of j ",key)
                    
                  

    print(templist)




    for i in range(len(newlist)):
        j = 1
        key = newlist[i]
        while j < len(key) :
            onenextitem= key[j]            
            z= j - 1
            oneprevitem= key[z]
            if onenextitem == oneprevitem :
                key.remove(onenextitem)
                print('value is ',onenextitem.index(onenextitem) ,"and key[z] is ",key.index(oneprevitem),"both is equal")
            j +=1
        else :
            print("tmp key is ",onenextitem)
            print("key[z]",oneprevitem)
            
    print(newlist)
    
    

    for i in tmp :
        for j in alphalist :
            if i.count(j) != 1 :
                print(j)
                templist = list(i)
                templist.remove(j)
                newlist.append("".join(templist))

    print(newlist)

    """
                
    
    
        





if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)