try:
    t=int(input())
    ans=0
    for i in range(t):
        n,k=map(int,input().split())
        for i in range(1,k+1):
            ans=max(ans,n%i)
            
        print(ans)
except:
    pass
