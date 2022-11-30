import sys
from collections import deque

read = sys.stdin.readline
N, M = map(int, read().split())
maze = [list(map(int, read().rstrip())) for _ in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue = deque([(0, 0)])
while queue:
    ny, nx = queue.popleft()
    for dir_y, dir_x in direction:
        my, mx = ny + dir_y, nx + dir_x
        if 0 <= my < N and 0 <= mx < M and maze[my][mx] == 1:
            queue.append((my, mx))
            maze[my][mx] = maze[ny][nx] + 1

print(maze[N - 1][M - 1])