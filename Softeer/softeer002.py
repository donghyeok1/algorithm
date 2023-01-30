import sys

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    sum_num = a + b
    print(f"Case #{i + 1}: {sum_num}")
