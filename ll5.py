try:
    t=int(input())

    for i in range(t):
        lst=[]
        n,k,d=map(int,input().split())

        tot=sum(map(int,input().split()))



        print(tot)
        if tot<k:
            print("0")
        else:
            res=tot//k
            if res>d:
                print(d)
            else:
                print(res)

except:
    pass