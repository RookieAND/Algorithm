import sys

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * M for i in range(N)]

dp[0][0] = maze[0][0]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + maze[i][0]
    
if M > 1:
    for j in range(1, M):
        for i in range(N):
            if i == 0:
                dp[0][j] = dp[0][j-1] + maze[0][j]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + maze[i][j]
print(dp[N-1][M-1])