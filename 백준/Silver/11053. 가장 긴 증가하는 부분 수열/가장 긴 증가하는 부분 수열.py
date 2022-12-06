import sys

read = sys.stdin.readline
N = int(read())
A = list(map(int, read().split()))

# dp[i] 는 인덱스 i 에서 시작할 경우 제작 가능한 수열의 최대 길이.
dp = [0] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))