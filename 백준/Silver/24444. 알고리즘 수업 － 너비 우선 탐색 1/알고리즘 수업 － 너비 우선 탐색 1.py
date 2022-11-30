import sys
from collections import deque

read = sys.stdin.readline
N, M, R = map(int, read().split())

visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

for idx in range(N + 1):
    graph[idx].sort()


queue = deque([R])
sequence = 1
visited[R] = 1
while queue:
    current = queue.popleft()
    for node in graph[current]:
        if not visited[node]:
            sequence += 1
            visited[node] = sequence
            queue.append(node)

print(*visited[1:], sep="\n")