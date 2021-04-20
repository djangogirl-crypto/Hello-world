def subset(set,sum,n):
    table=[[False for i in range(sum+1)] for i in range(n+1)]
    for i in range(1,sum+1):
        table[0][i]=False
    for i in range(n+1):
        table[i][0]=True
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if set[i-1]<=j:
                table[i][j]= table[i-1][j-set[i-1]] or table[i-1][j]
            else:
                table[i][j]=table[i-1][j]
    return table[n][sum]
set=[3,34,4,12,5,2]
n=len(set)
sum=9
print(subset(set,sum,n))

