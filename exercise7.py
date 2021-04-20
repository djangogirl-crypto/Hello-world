import random
user_num= int(input('enter a number:'))
mynum= random.randint(1,9)
print(mynum)
if user_num==mynum:
    print('exact')
elif user_num>mynum:
    print('high')
else:
    print('low')
