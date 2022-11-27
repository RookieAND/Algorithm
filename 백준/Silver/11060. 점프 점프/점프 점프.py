import sys
from collections import deque

read = sys.stdin.readline
N = int(read())
maze = list(map(int, read().split()))
visited = [-1] * N

def bfs(start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        cur_loc = queue.popleft()
        if maze[cur_loc] > 0:
            for loc in range(1, maze[cur_loc] + 1):
                next_loc = cur_loc + loc
                if 0 <= next_loc < N:
                    if visited[next_loc] > visited[cur_loc] + 1 or visited[next_loc] == -1:
                        visited[next_loc] = visited[cur_loc] + 1
                        queue.append(next_loc)

    return visited[N - 1]

print(bfs(0))