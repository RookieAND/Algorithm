import sys
from collections import deque

read = sys.stdin.readline
N, M, V = map(int, read().split())

graph = [list() for _ in range(N + 1)]

for _ in range(M):
    f_node, s_node = map(int, read().split())
    graph[f_node].append(s_node)
    graph[s_node].append(f_node)

# 작은 노드부터 우선 탐색해야 하므로, 그래프를 1차적으로 정렬해야 함.
graph = [sorted(graph[i]) for i in range(N + 1)]

# DFS 탐색 함수, 재귀 함수를 사용하여 반복 실행된다.
def dfs(start, visited):
    visited[start] = True
    print(start, end=" ")
    for node in graph[start]:
        if not visited[node]:
            dfs(node, visited)


visited = [False] * (N + 1)
dfs(V, visited)
print("", end="\n")


# BFS 탐색 함수, Queue를 사용한다는 것을 잊지 말자.
def bfs(start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True


visited = [False] * (N + 1)
bfs(V, visited)

