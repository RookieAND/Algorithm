import sys

read = sys.stdin.readline
N, K = map(int, read().split())
A = list(map(int, read().split()))

# 최대로 정렬을 진행할 index를 1부터 N - 1 까지 오름차순으로 진행.
count = 0
for idx in range(1, N):
    loc = idx - 1
    new_item = A[idx]
    # loc은 정렬을 진행할 index, new_item의 경우 저장된 값.
    # loc이 0 이상이면서 현재 정렬할 위치의 값이 저장된 값보다 클 경우, 정렬 진행.
    while loc >= 0 and new_item < A[loc]:
        A[loc + 1] = A[loc]
        loc -= 1
        count += 1
        if count == K:
            print(A[loc + 1])
            sys.exit(0)
    # 반복 정렬을 마친 후, 조금이라도 정렬이 진행되었다면 저장된 값을 업데이트.
    if loc + 1 != idx:
        A[loc + 1] = new_item
        count += 1
        if count == K:
            print(A[loc + 1])
            sys.exit(0)
print(-1)
