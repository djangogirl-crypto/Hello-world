def editDistance(str1,str2):
    m=len(str1)
    n=len(str2)
    l=[[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                l[i][j]=j
            elif j==0:
                l[i][j]=i
            elif str1[i-1]==str2[j-1]:
                l[i][j]=l[i-1][j-1]
            else:
                l[i][j]=min(l[i-1][j],l[i][j-1])+1
    return l[m][n]
print(editDistance("heap","pea"))