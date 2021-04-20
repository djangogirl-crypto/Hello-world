import sys
def partition(arr,n):
    su=sum(arr)
    table=[[0 for i in range(su+1)] for i in range(n+1)]
    for i in range(1,su+1):
        table[0][i]=False
    for i in range(n+1):
        table[i][0]=True
    for i in range(n+1):
        for j in range(su+1):
            if arr[i-1]<=j:
                table[i][j]=table[i-1][j] or table[i-1][j-arr[i-1]]
            else:
                table[i][j]=table[i-1][j]
    diff=sys.maxsize
    for j in range(su//2,-1,-1):
        if table[n][j]==True:

            diff=su-(2*j)
            break
    return diff
arr=[3,1,4,2,2,1]
n=len(arr)

print(partition(arr,n))