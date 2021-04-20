num= int(input('enter a number'))
x=[]
for i in range(1,num+1):
    if num%i ==0:
        x.append(i)
print(x)