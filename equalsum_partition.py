def subset(set,sum,n):
    table=[[False for i in range(sum+1)] for i in range(n+1)]
    for i in range(1,sum+1):
        table[0][i]=False
    for i in range(n+1):
        table[i][0]=True
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if set[i-1]<=j:
                table[i][j]=table[i-1][j] + table[i-1][j-set[i-1]]
            else:
                table[i][j]=table[i-1][j]
    return table[n][sum]
set=[2,3,4,1,8]
sum=10

n=len(set)
print(subset(set,sum,n))

