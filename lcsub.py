def lcsub(x,y,m,n):
    table=[[0 for i in range(m+1)] for i in range(n+1)]
    result=0
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                table[i][j]=0
            elif x[i-1] == y[j-1]:
                table[i][j]=table[i-1][j-1]+1
                result=max(result,table[i][j])
            else:
                table[i][j]=0
    return result

x="abcxyz"
y="xyzabc"
m=len(x)
n=len(y)
print(lcsub(x,y,m,n))