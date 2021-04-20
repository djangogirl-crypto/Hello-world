# cook your dish here
t=int(input())
n=input()
arr=list(map(int,input().split()))

h=max(arr)-1
count=0
while(all(arr)==True):
    for i in range(len(arr)):
        if i>h:
            i=h
            count+=1
            h=h-1
print(count)
