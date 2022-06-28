import sys
from collections import deque

read = sys.stdin.readline
N, M = map(int, read().split())
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

matrix, land_locs = [], []
for row in range(N):
    mat_row = list(read().strip())
    for col in range(M):
        if mat_row[col] == 'L':
            land_locs.append((row, col))
    matrix.append(mat_row)


# 두 좌표를 tuple로 받는 bfs 탐색 함수 선언.
def bfs(y, x):
    # 방문 여부를 판별하는 이차원 배열을 새롭게 생성.
    visited = [[-1] * M for _ in range(N)]
    visited[y][x] = 0
    queue, distance = deque([(y, x)]), 0
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my, mx = ny + direct[0], nx + direct[1]
            # 만약 탐색된 좌표가 유효 범위 이내이며, 아직 미방문된 곳인지 판별.
            if 0 <= my < N and 0 <= mx < M:
                if visited[my][mx] == -1 and matrix[my][mx] == 'L':
                    queue.append((my, mx))
                    visited[my][mx] = visited[ny][nx] + 1
                    distance = max(visited[my][mx], distance)

    return distance


result = 0
# 모든 육지의 좌표를 하나씩 순화하며 나온 최단 거리 비교
for land_loc in land_locs:
    loc_y, loc_x = land_loc
    result = max(result, bfs(loc_y, loc_x))

print(result)
