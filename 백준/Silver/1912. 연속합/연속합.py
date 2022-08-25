import sys

read = sys.stdin.readline
N = int(read())
number = list(map(int, read().split()))
dp = [0] * N
dp[0] = number[0]

for i in range(1, N):
    dp[i] = max(dp[i-1] + number[i], number[i])

print(max(dp))