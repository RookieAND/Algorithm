import sys

n, m = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))
sumList, result = [0 for i in range(n+1)], []

# sumList[i] 는 numList의 요소를 0번째부터 i번째까지 합산한 값을 저장함
# 각 인덱스까지의 합을 미리 저장해두면, 추후 구간 별 부분합을 산출할 때 더 빠름.
for i in range(1, n+1):
    sumList[i] = sumList[i-1] + numList[i-1]

for _ in range(m):
    # numList의 i번째부터 j번째까지의 합을 구하고 싶다면, 미리 계산해둔 sumList를 사용
    # numList에서, 0부터 j번째까지의 합에서 0부터 i-1번짜까지의 합을 빼면 i부터 j까지의 합이 나옴.
    i, j = map(int, sys.stdin.readline().split())
    result.append(sumList[j] - sumList[i-1])
print(*result, sep="\n")