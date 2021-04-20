from datetime import datetime,timedelta
try:
    t = int(input())
    for i in range(t):
        nw = input().split(" ")
        h,m =nw[0].split(":")

        n = int(input())
        for i in range(n):
            lst = input().split(" ")
            h1, m1 = lst[0].split(":")
            h2, m2 = lst[2].split(":")
            print(h1,h2)

            zero = timedelta(int(m) * 60 + int(h) * 3600)
            print(zero)
            st = nw - zero  # tis take me to 0 hours.
            print(st)
            time1 = st + timedelta(seconds=int(h1) * 3600 + int(m1) * 60)  # this gives 10:30 AM
            time2 = st + timedelta(seconds=int(h2) * 3600 + int(m2) * 60)  # this gives 4:30 PM
            print(time1)
            print(time2)
            print(nw)
            if nw >= time1 and nw <= time2:
                print("1")
            else:
                print("0")

except:
    pass