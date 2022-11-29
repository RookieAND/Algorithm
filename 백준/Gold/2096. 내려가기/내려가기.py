import sys

read = sys.stdin.readline
N = int(read())
min_dp = [0] * 3
max_dp = [0] * 3

# 모든 값을 메모이제이션 하지 않고, 기존의 메모이제이션 값을 갱신하는 식으로 진행.
for _ in range(N):
    a, b, c = list(map(int, read().split()))
    # 직전의 열까지의 계산을 통해, 각 행에 대한 최대 / 최소 값을 사용하여 DP 실행.
    max_dp = [max(max_dp[0], max_dp[1]) + a, max(max_dp[0], max_dp[1], max_dp[2]) + b, max(max_dp[1], max_dp[2]) + c]
    min_dp = [min(min_dp[0], min_dp[1]) + a, min(min_dp[0], min_dp[1], min_dp[2]) + b, min(min_dp[1], min_dp[2]) + c]

print(max(max_dp), min(min_dp))