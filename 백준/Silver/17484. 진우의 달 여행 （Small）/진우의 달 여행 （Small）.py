import sys
from math import inf
read = sys.stdin.readline

N, M = map(int, read().split())
matrix = [list(map(int, read().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(M)]] + [[[float('inf'),float('inf'),float('inf')] for _ in range(M)] for _ in range(N)]

for i in range(1, N+1):
    for j in range(M):
        if j < M-1:
            dp[i][j][0] = min(dp[i-1][j+1][1],dp[i-1][j+1][2]) + matrix[i-1][j]
        if 0 < j:
            dp[i][j][2] = min(dp[i-1][j-1][1],dp[i-1][j-1][0]) + matrix[i-1][j]
        dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2]) + matrix[i-1][j]

min_value = inf
for row in dp[i]:
    for value in row:
        min_value = min(min_value, value)
print(min_value)