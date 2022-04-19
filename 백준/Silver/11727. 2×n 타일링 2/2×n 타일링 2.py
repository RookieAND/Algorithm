import sys

n = int(sys.stdin.readline())
dp = [0] * 1001
dp[0], dp[1] = [1, 1]

# i번째 타일을 만들기 위해서는 i-1번째 타일에서 1x2 타일을 더 붙인 케이스가 있다. (dp[i-1)
# 또한 i-2 번째 타일에서 2x2 타일 또는 1x2 타일을 2개 붙이면 된다. (dp[i-2] * 2)
# 따라서 점화식은 dp[i] = dp[i-1] + dp[i-2] * 2 와 같다.
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2
sys.stdout.write(str(dp[n] % 10007))