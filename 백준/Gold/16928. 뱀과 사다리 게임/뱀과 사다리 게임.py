import sys
from collections import deque

read = sys.stdin.readline
N, M = map(int, read().split())
boards = dict()
visited = [0] * 101


for _ in range(N):
    x, y = map(int, read().split())
    boards[x] = y

for _ in range(M):
    u, v = map(int, read().split())
    boards[u] = v

queue = deque([1])
while queue:
    if visited[100] > 0:
        print(visited[100])
        sys.exit(0)
    loc = queue.popleft()
    for i in range(1, 7):
        new_loc = loc + i if loc + i not in boards else boards[loc + i]
        if 1 <= new_loc <= 100:
            if visited[new_loc] == 0 or visited[new_loc] > visited[loc] + 1:
                visited[new_loc] = visited[loc] + 1
                queue.append(new_loc)