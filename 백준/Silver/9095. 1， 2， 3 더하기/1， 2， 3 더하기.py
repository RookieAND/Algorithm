import sys

N = int(sys.stdin.readline())
cases = [int(sys.stdin.readline().strip()) for _ in range(N)]

dp = [0, 1, 2, 4] + [0] * 7

for i in range(4, 11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

list(map(lambda x: print(dp[x]), cases))