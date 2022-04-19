import sys

# P(1) ~ P(100) 까지 해당되는 모든 수를 우선 구해놓는다.
dp = [0] * 101
dp[1], dp[2], dp[3], dp[4] = 1, 1, 1, 2
for i in range(5, 101):
    dp[i] = dp[i-1] + dp[i-5]

result = []
for _ in range(int(sys.stdin.readline())):
    result.append(dp[int(sys.stdin.readline())])
print(*result, sep="\n")