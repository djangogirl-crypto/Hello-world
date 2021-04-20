try:
    t=int(input())
    lst=[]
    for i in range(t):
        arr=list(map(int,input().split()))
        arr.remove(arr[0])
        print(arr)
        m=min(arr)
        print(m)
        for i in range(len(arr)+1):
            k=int(arr[i]) // m
            lst.append(k)
        print(lst)
except:
    pass
