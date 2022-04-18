import sys

N = int(sys.stdin.readline())
wine = [0] + [int(sys.stdin.readline()) for _ in range(N)]

# N이 3 미만일 경우 경우의 수가 다름, 예외 처리
if N <= 3:
    if N == 1:
        print(wine[1])
    elif N == 2:
        print(wine[1] + wine[2])
    elif N == 3:
        print(max(wine[1] + wine[3], wine[2] + wine[3], wine[1] + wine[2]))
else:
    dp = [0] * (N+1)
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    for i in range(3, N+1):
        dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])
    print(dp[N])