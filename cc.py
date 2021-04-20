try:


    def clglife(n, wt, val):
        dp = [0 for i in range(n + 1)]
        ans = 0
        for i in range(n + 1):
            for j in range(len(val)):
                if wt[j] <= i:
                    dp[i] = min(dp[i], dp[i - wt[j] + val[j]])
        return dp[n]


    def note(n, e, h, c):
        if n >= e:
            return (e * c)


    t = int(input())
    print(t)
    for i in range(t):
        n, e, h, a, b, c = input().split()
        wt = list(e, h)
        val = list(a, b)
        print(min(clglife(n, wt, val), note(n, e, h, c)))


except:
    pass
