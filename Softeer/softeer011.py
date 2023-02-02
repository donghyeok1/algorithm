import sys

# def fun(c, n):
#     if n == 1:
#         return c
    
#     else:
#         x = fun(c, n // 2)
#         if n % 2 == 0:
#             return x * x
#         else:
#             return x * x * c

k, p, n = map(int, sys.stdin.readline().split())

# print((k * fun(p, n)) % 1000000007)

# 분할 정복 생각했는데, 분할 정복이 아니라 나머지 정리의 분배 법칙 이용해야함.

for i in range(n):
    k = k * p % 1000000007

print(k)