N = int(input())
A = list(map(int, input().split()))

# 가장 긴 증가하는 부분 수열의 길이를 담을 메모이제이션
dp = [1] * N

for i in range(N):
    for j in range(i):
        # i 보다 작은 숫자들 중에서 수열의 길이에 대한 업데이트 진행.
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 길이부터 먼저 출력시킨다.
max_length = max(dp)
print(max_length)

# 이후 dp 배열을 순차적으로 순회하면서, 가장 긴 증가하는 부분 수열을 찾는다.
# 단, 역순으로 찾아야 올바른 순서대로 부분 수열의 내용물을 알 수 있다.
result, rank = [], max_length

for idx in range(len(dp) - 1, -1, -1):
    if dp[idx] == rank:
        result.append(A[idx])
        rank -= 1
print(*result[::-1])