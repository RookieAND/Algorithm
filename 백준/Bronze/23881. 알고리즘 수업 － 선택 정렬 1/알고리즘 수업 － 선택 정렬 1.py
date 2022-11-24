import sys

read = sys.stdin.readline
N, K = map(int, read().split())
A = list(map(int, read().split()))

# 최대로 정렬을 진행할 index를 N - 1부터 1까지 내림차순으로 진행.
count = 0
for idx in range(N - 1, 0, -1):
    max_value = max(A[:idx + 1])
    max_value_idx = A.index(max_value)
    # 정렬 대상 범주 내에서, 가장 끝에 위치한 값이 최대가 아닐 경우 교환.
    if max_value != A[idx]:
        A[idx], A[max_value_idx] = A[max_value_idx], A[idx]
        count += 1
        if count == K:
            print(A[max_value_idx], A[idx])
            sys.exit(0)
print(-1)