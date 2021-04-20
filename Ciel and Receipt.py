for i in range(int(input())):
    lst = [2048,1024,512,256,128,64,32,16,8,4,2,1]
    n=int(input())
    while n>0:
        cnt=0
        for i in lst:
            if n>=i:
                d=n//i
                cnt+=d
                n=n%i
    print(cnt)





