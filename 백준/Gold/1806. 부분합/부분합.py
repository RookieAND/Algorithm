import sys
from math import inf

read = sys.stdin.readline
N, S = map(int, read().split())
numbers = list(map(int, read().split()))

start, end = 0, 0
max_sum = numbers[0]
result = inf

while True:
    # 부분합이 S 보다 작을 경우, 범위를 끝으로 1 증가
    if max_sum < S:
        end += 1
        # 만약 끝 포인터가 마지막에 다다랐다면, 탐색 중단.
        if end == N:
            break
        # 누적 합에 우측 값을 추가시킴.
        max_sum += numbers[end]
    # 부분합이 S 보다 클 경우, 범위를 시작에서 1 감소
    else:
        result = min(result, end - start + 1)
        max_sum -= numbers[start]
        start += 1

print(result if result != inf else 0)