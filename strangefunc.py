t=int(input())
for i in range(t):
    n=int(input())
    sum=0
    cnt=0
    for i in range(1,n+1):
        if sum!=n:
            if sum>n:
                sum-=1
            else:
                sum+=i

        cnt+=1
    print(cnt)