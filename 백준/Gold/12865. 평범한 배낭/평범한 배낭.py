import sys

N, K = map(int, sys.stdin.readline().split())
object = [(0, 0)] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight, value = object[i]
        if j >= weight:
            dp[i][j] = max(dp[i - 1][j], dp[i-1][j-weight] + value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])