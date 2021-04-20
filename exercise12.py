def get_int():
    num= int(input('enter  number of elem:'))
    return num
def fib(nums):
    a,b=0,1
    for i in range(0,nums):
        a,b=b,a+b
        print(a)

number=get_int()
fib(number)