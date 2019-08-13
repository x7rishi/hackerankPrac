
def merge_the_tools(string,k):
    n = len(string)
    divchecker = lambda n,k : n%k == 0
    if divchecker(n,k) :
        temp = list()
        for i in range(n):
            if i%k == 0:
                temp.append(string[i:i+k])
        newlist = list()
        for ch in temp :
            newlist.append(list(ch))
            # Here newlist variable is [['A', 'A', 'B'], ['C', 'A', 'A'], ['A', 'D', 'A']]

        # this part is used from the https://www.w3schools.com/python/python_howto_remove_duplicates.asp
        for gh in newlist :
            t=(list(dict.fromkeys(gh)))
            z= "".join(t)
            print(z)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)