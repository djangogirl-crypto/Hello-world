n=20
prime=[True]*(n+1)
def sieveOfErathosthenes():
    p=2
    while p*p<=n:
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    for p in range(2,n+1):
        if prime[p]:
            print(p)

sieveOfErathosthenes()