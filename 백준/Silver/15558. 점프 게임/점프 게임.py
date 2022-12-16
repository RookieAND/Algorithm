from sys import stdin
from collections import deque


def can_visited(x, y, i):
    return i < y < N and matrix[x][y] and not visited[x][y]


def bfs(start):
    queue = deque([start])
    current_idx = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for nx, ny in ((x, y + 1), (x, y - 1), (~x, y + K)):
                if ny >= N:
                    return 1
                if can_visited(nx, ny, current_idx):
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        current_idx += 1
    return 0


N, K = map(int, (stdin.readline().split()))
visited = [[False] * N for _ in range(2)]
matrix = [list(map(int, stdin.readline().strip())) for _ in range(2)]
print(bfs([0, 0]))