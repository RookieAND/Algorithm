import sys
from math import inf
from collections import deque

read = sys.stdin.readline
N = int(read())

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
matrix = []
min_height, max_height = inf, 0

for _ in range(N):
    row = list(map(int, read().split()))
    min_height = min(min_height, min(row))
    max_height = max(max_height, max(row))
    matrix.append(row)


def bfs(y, x, h):
    global visited
    queue = deque([(y, x)])
    visited[y][x] = True
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my, mx = ny + direct[0], nx + direct[1]
            if 0 <= my < N and 0 <= mx < N:
                if not visited[my][mx] and matrix[my][mx] > h:
                    visited[my][mx] = True
                    queue.append((my, mx))


def find_safe_area(height):
    global visited
    areas = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and matrix[i][j] > height:
                bfs(i, j, height)
                areas += 1
    return areas

# 어떤 곳도 물에 잠기지 않았을 경우에는 최소 안전지대가 1이다.
result = 1
for height in range(min_height, max_height + 1):
    visited = [[False] * N for _ in range(N)]
    result = max(result, find_safe_area(height))

print(result)