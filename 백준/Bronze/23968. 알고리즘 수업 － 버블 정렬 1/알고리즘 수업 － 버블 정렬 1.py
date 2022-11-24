import sys

read = sys.stdin.readline
N, K = map(int, read().split())
A = list(map(int, read().split()))

# 최대로 정렬을 진행할 index를 N - 1부터 1까지 내림차순으로 진행.
count = 0
for idx in range(N - 1, 0, -1):
    # index 0 부터 최대 정렬을 진행할 index 직전까지, 버블 정렬 수행.
    for i in range(idx):
        if A[i] > A[i + 1]:
            A[i + 1], A[i] = A[i], A[i + 1]
            count += 1
        if count == K:
            print(A[i], A[i + 1])
            sys.exit(0)

print(-1)