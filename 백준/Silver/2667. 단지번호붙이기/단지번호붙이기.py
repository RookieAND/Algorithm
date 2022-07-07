import sys
from collections import deque

read = sys.stdin.readline
N = int(read())

matrix = [list(map(int, read().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(y, x):
    count = 1
    queue = deque([(y, x)])
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my, mx = ny + direct[0], nx + direct[1]
            if 0 <= my < N and 0 <= mx < N:
                if matrix[my][mx] and not visited[my][mx]:
                    visited[my][mx] = True
                    count += 1
                    queue.append((my, mx))
    return count


result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and matrix[i][j]:
            visited[i][j] = True
            result.append(bfs(i, j))

result.sort()
print(len(result), *result, sep='\n')
