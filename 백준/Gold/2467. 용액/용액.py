import sys
from math import inf

read = sys.stdin.readline
N = int(read())
composites = list(map(int, read().split()))

result = [None, None, inf]
start, end = 0, N - 1

while start < end:
    mid = composites[start] + composites[end]
    if mid == 0:
        print(composites[start], composites[end])
        sys.exit(0)
    if abs(mid) <= abs(result[2]):
        result = [composites[start], composites[end], mid]
    # 혼합 용액이 양수이므로, 끝 범위를 줄여야 함
    if mid > 0:
        end -= 1
    else:
        start += 1

print(*result[:2])

