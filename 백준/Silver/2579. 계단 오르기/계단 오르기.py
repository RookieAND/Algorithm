import sys

N = int(sys.stdin.readline())
pts = [0] + [int(sys.stdin.readline()) for _ in range(N)]

if N <= 2:
    if N == 1:
        print(pts[1])
    elif N == 2:
        print(pts[1] + pts[2])
else:
    dp = [0] * (N+1)
    dp[1], dp[2], dp[3] = pts[1], (pts[1] + pts[2]), max(pts[1], pts[2]) + pts[3]
    for i in range(4, N+1):
        dp[i] = (max(dp[i-2], dp[i-3] + pts[i-1]) + pts[i])
    print(dp[-1])