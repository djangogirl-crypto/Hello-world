num= int(input('enter a number: '))
a=[x for x in range(2,num//2+1) if num%x==0]
if num>1:
    if len(a)==0 :
        print('prime')
    else:
        print('not prime')
