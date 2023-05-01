def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    
    dp[2] = 3
    if n % 2 == 1:
        return 0
    elif n == 2:
        return 3
    else:
        for i in range(4, n + 1, 2):
            dp[i] = dp[i - 2] * 3 + sum(dp[2 : i - 2]) * 2 + 2
        
    return dp[n] % 1000000007