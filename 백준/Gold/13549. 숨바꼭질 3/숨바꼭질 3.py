import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [-1] * 100001

def bfs(start):
    visited[start] = 0
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == K:
            break
        for nd in [current * 2, current - 1, current + 1]:
            if 0 <= nd <= 100000 and visited[nd] == -1:
                if nd == current * 2:
                    visited[nd] = visited[current]
                    queue.appendleft(nd)
                else:
                    visited[nd] = visited[current] + 1
                    queue.append(nd)
    return visited[K]

print(bfs(N))