def knapsack(W,wt,val,n):
    table=[[0 for i in range(W+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                table[i][j]=0
            elif wt[i-1] <= j:
                table[i][j]=max(val[i-1]+table[i-1][j-wt[i-1]],table[i-1][j])
            else:
                table[i][j] = table[i - 1][j]
    return table[n][W]
wt=[10,20,30]
val=[60,100,120]
n=len(val)
W=50
c=knapsack(W,wt,val,n)
print(c)


