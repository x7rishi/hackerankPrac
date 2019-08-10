#https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    n = len(string)
    # printing the  n/k  line where each line i contains string ui.
    tmp = list()
    for i in range(n):
        if i%k == 0:

            tmp.append(string[i:i+k])
    print(tmp)
    for i in range(len(tmp)):
        print(i)





if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)