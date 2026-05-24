def maxCuts(n, a, b, c):
    NEG = float('-inf')
    dp = [NEG]*(n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for cut in (a, b, c):
            if i >= cut and dp[i-cut] != NEG:
                dp[i] = max(dp[i], dp[i-cut] + 1)
    if dp[n] != NEG:
        return dp[n] 
    else:
        0

print(maxCuts(5, 5, 2, 1))