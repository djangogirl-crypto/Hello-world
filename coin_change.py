def coinchange(arr,m,n):#n=len(arr) m=sum
    l=[[0 for x in range(m+1)] for x in range(n+1)]
    for i in range(n+1):
        l[i][0]=1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if arr[i-1]>j:
                l[i][j]=l[i-1][j]
            else:
                l[i][j]=l[i-1][j]+l[i][j-arr[i-1]]

    return l[n][m]
arr=[1,2,5]
m=5
print(coinchange(arr,m,len(arr)))