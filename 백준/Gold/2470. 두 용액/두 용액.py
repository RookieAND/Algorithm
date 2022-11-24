import sys
from math import inf

read = sys.stdin.readline
N = int(read())
liquids = sorted(list(map(int, read().split())))
start, end, result = 0, N - 1, [inf, [liquids[0], liquids[-1]]]

while start < end:
    composite = liquids[start] + liquids[end]
    # 혼합 용액의 특성 값이 기존의 결과보다 작거나 같다면, 결과 값을 업데이트.
    if abs(composite) < result[0]:
        result = [abs(composite), [liquids[start], liquids[end]]]
    # 시작과 끝의 합산 값이 음수라면 시작 범위를 줄이고, 양수라면 끝 범위를 줄인다.
    if composite < 0:
        start += 1
    else:
        end -= 1

print(result[1][0], result[1][1])

