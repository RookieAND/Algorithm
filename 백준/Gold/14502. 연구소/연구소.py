import sys, copy
from collections import deque
import itertools as iters

read = sys.stdin.readline
N, M = map(int, read().split())

graph = [list(map(int, read().split())) for _ in range(N)]
empty_place = []

for row in range(N):
    for col in range(M):
        if graph[row][col] == 0:
            empty_place.append((row, col))

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def virus_spread(y, x):
    queue = deque([(y, x)])
    temp_graph[y][x] = 2
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my = ny + direct[0]
            mx = nx + direct[1]
            # 이동한 좌표가 유효 범위 내에 있고, 아직 퍼지지 않은 곳인지 판별
            if (0 <= my < N and 0 <= mx < M) and not temp_graph[my][mx]:
                temp_graph[my][mx] = 2
                queue.append((my, mx))


def get_safety_area():
    size = 0
    for row_list in temp_graph:
        size += row_list.count(0)
    return size


max_size = 0
# 전체 빈 공간에서, 무작위하게 3곳을 선택하여 벽을 세움.
for loc_list in iters.combinations(empty_place, 3):
    # 벽을 세운 후의 연구소 모양을 deepcopy로 깊은 복사하여 가져옴.
    temp_graph = copy.deepcopy(graph)
    # 랜덤으로 선택된 좌표 세 곳에 벽을 새롭게 세움.
    for loc in loc_list:
        y, x = loc
        temp_graph[y][x] = 1

    # 연구소 공간을 순회하면서, 바이러스가 있다면 주변 영역을 감염시킴.
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 2:
                virus_spread(i, j)

    # 감염이 진행된 후, 빈 공간을 구하여 최댓값과 비교함
    size = get_safety_area()
    max_size = max(max_size, size)

print(max_size)