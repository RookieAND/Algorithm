import sys
from collections import deque

read = sys.stdin.readline
N = int(read())
graph = [list() for _ in range(N + 1)]
for i in range(int(read())):
    f_node, s_node = map(int, read().split())
    graph[f_node].append(s_node)
    graph[s_node].append(f_node)


visited = [False] * (N + 1)
def bfs(node):
    visited[node] = True
    result = 0
    queue = deque([node])
    while queue:
        nd = queue.popleft()
        if graph[nd]:
            for new_nd in graph[nd]:
                if not visited[new_nd]:
                    queue.append(new_nd)
                    visited[new_nd] = True
                    result += 1
    return result

print(bfs(1))


