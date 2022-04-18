import sys

N = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(N+1)]
dp[1] = [1] * 10

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][j] = sum(dp[i-1][0:j+1])
print(sum(dp[N]) % 10007)