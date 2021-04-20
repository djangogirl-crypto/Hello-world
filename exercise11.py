def listEnds(l):
    return(l[0],l[len(l)-1])

n=int(input('enter a no. of elements in list:'))
l=[]
for i in range (1,n+1):
    num= int(input('enter number:'))
    l.append(num)

print(l)



result1,result2=listEnds(l)
print(result1,result2)

