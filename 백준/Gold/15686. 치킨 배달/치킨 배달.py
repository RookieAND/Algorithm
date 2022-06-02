import sys
from math import inf
from itertools import combinations as comb

read = sys.stdin.readline
N, M = map(int, read().split())
house_list, chicken_list = [], []

for i in range(N):
    row_list = list(map(int, read().split()))
    for j in range(N):
        if row_list[j] == 1:
            house_list.append((i, j))
            continue
        if row_list[j] == 2:
            chicken_list.append((i, j))

result = inf
# 각 치킨 집의 목록 중에서, M개를 무작위하게 추출함.
for chicken_locs in comb(chicken_list, M):
    min_length = 0
    # 각 집을 순회하며 치킨집 별 치킨 거리를 계산함.
    for house_loc in house_list:
        chicken_len = inf
        # M개로 추출된 치킨집 중에서, 가장 적은 값의 치킨 거리를 찾는 과정
        for chicken_loc in chicken_locs:
            between_len = abs(house_loc[0] - chicken_loc[0]) + abs(house_loc[1] - chicken_loc[1])
            chicken_len = min(chicken_len, between_len)
        min_length += chicken_len
    # 합산하여 나온 도시의 치킨 거리가, 기존의 값보다 작은지 대조
    result = min(result, min_length)
print(result)