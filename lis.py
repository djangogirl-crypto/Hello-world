def lis(arr):
    n=len(arr)
    l=[1 for i in range(len(arr))]
    for i in range(1,n):
        for j in range(0,i+1):
            if arr[i]>arr[j] and l[i]<l[j]+1:
                l[i]=l[j]+1
    maxim=0

    for i in range(n):
        maxim=max(maxim,l[i])
    return maxim
arr=[3,4,-1,0,6,2,3]
print(lis(arr))
