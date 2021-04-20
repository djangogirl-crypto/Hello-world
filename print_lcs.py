def lcs(x,y,m,n):
    t=[[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif t[i-1]==t[j-1]:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    index=t[m][n]
    lcs=[""]*(index+1)
    lcs[index]=""
    i=m
    j=n
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            lcs[index-1]=x[i-1]
            i-=1
            j-=1
            index-=1
        elif t[i-1][j]>t[i][j-1]:
            i-=1
        else:
            j-=1
    print("".join(lcs))
x="aggtab"
y="gxtxayb"
m=len(x)
n=len(y)
lcs(x,y,m,n)
