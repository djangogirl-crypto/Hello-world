def lcs(X,Y):
    m=len(X)
    n=len(Y)
    lst=[[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                lst[i][j]=0
            elif X[i-1]==Y[j-1]:
                lst[i][j]=lst[i-1][j-1]+1
            else:
                lst[i][j]=max(lst[i-1][j],lst[i][j-1])
    return lst[m][n]
X="aggtab"
Y="gxtxayb"
print(lcs(X,Y))