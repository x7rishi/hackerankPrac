def miniMaxSum(arr):
    arr.sort()
    smin = smax = 0
    smin = sum(arr) - arr[-1]
    smax = sum(arr) - arr[0]
    print(smin,smax,sep = ' ',end='')
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
