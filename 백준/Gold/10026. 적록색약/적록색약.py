import copy
import sys
from collections import deque

read = sys.stdin.readline
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N = int(read())
picture = [list(read().strip()) for _ in range(N)]
picture_rg = [[0] * N for _ in range(N)]

# 적록색약의 경우, 초록색을 빨간색으로 본다고 가정하고 진행.
for i in range(N):
    for j in range(N):
        picture_rg[i][j] = 'R' if picture[i][j] == 'G' else picture[i][j]


visited = [[False] * N for _ in range(N)]


# 너비 탐색으로 같은 색상을 찾고, 이를 모두 방문 처리 (visited) 시킴.
def bfs(y, x, graph):
    visited[y][x] = True
    color = graph[i][j]
    queue = deque([(y, x)])
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my = ny + direct[0]
            mx = nx + direct[1]
            # 만약 유효 범위 내에 이동된 좌표가 해당되는지를 판별.
            if 0 <= my < N and 0 <= mx < N:
                # 아직 방문하지 않았고, 동일한 색상이라면 이를 방문 처리 시킴.
                if not visited[my][mx] and graph[my][mx] == color:
                    queue.append((my, mx))
                    visited[my][mx] = True

# 일반 사용자의 케이스를 먼저 조사함.
amount = 0
for i in range(N):
    for j in range(N):
        # 적록 색약이 아닐 경우, 연결 요소를 파악함.
        if not visited[i][j]:
            bfs(i, j, picture)
            amount += 1

# 적록 색약의 케이스를 추가로 조사해야 함.
amount_rg = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        # 적록 색약이 아닐 경우, 연결 요소를 파악함.
        if not visited[i][j]:
            bfs(i, j, picture_rg)
            amount_rg += 1

print(amount, amount_rg)