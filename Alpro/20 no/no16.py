def maxMango(f):
    if not f: return 0
    if len(f) == 1: return f[0]
    dp = [0]*len(f)
    dp[0], dp[1] = f[0], max(f[0], f[1])
    for i in range(2, len(f)):
        dp[i] = max(dp[i-1], dp[i-2] + f[i])
    return dp[-1]

print(maxMango([2, 7, 9, 3, 1]))