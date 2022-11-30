import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

read = sys.stdin.readline
N, M, V = map(int, read().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

graph = [sorted(graph[i]) for i in range(N + 1)]

def dfs(x):
    visited[x] = True
    print(x, end=" ")
    for node in graph[x]:
        if not visited[node]:
            dfs(node)

def bfs(x):
    queue = deque([x])
    visited[x] = True
    while queue:
        current = queue.popleft()
        print(current, end=" ")
        for node in graph[current]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True

visited = [False] * (N + 1)
dfs(V)
print("")
visited = [False] * (N + 1)
bfs(V)