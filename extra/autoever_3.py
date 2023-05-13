import sys


n, m = map(int, input().split()); 
car = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + car[i - 1]

answer = 0

for _ in range(m):
    s, t = map(int, sys.stdin.readline().split())
    answer += dp[t] - dp[s - 1]

print(answer)
print(dp)


# 5, 2
# 1 0 0 1 1
# 1 3
# 2 5