import sys

read = sys.stdin.readline
A, B = read().rstrip(), read().rstrip()


# dp[i][j] : A 문자열이 j번째까지, B 문자열이 i번째까지 존재할 때 가장 긴 부분 문자열.
dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

answer = 0
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)

print(answer)