import sys
from collections import deque

read = sys.stdin.readline
N, M, K = map(int, read().split())
matrix = [[0] * M for _ in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(K):
    f_x, f_y, l_x, l_y = map(int, read().split())
    for y in range(f_y, l_y):
        for x in range(f_x, l_x):
            matrix[y][x] = 1

def bfs(loc_y, loc_x):
    queue = deque([(loc_y, loc_x)])
    matrix[loc_y][loc_x] = 1
    expand = 1
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my, mx = ny + direct[0], nx + direct[1]
            if (0 <= my < N and 0 <= mx < M) and not matrix[my][mx]:
                queue.append((my, mx))
                matrix[my][mx] = 1
                expand += 1

    return expand

result = 0
result_expand = []
for i in range(N):
    for j in range(M):
        if not matrix[i][j]:
            result_expand.append(bfs(i, j))
            result += 1
print(result)
print(*sorted(result_expand))
