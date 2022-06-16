import sys

read = sys.stdin.readline
N = int(read())
P = [0] + list(map(int, read().split()))
dp = [0] * (N + 1)

dp[1] = P[1]
dp[2] = max(dp[1] + P[1], P[2])

# 점화식 : dp[i] = max(dp[i-1] + P[1], dp[i-2] + P[2], ..., P[i])
for i in range(3, N + 1):
    # dp[i-j] + P[j] 를 반복하여 가장 큰 값을 메모이제이션에 추가.
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i-j] + P[j])
        
print(dp[N])