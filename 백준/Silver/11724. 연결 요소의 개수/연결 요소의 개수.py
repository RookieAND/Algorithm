import sys
from collections import deque

read = sys.stdin.readline

# 입력 받은 정보를 토대로 각 노드 별로 연결된 노드들을 list로 표현.
# 즉, graph[i] 는 i번째 노드와 연결된 노드들의 집합을 의미한다.
N, M = map(int, read().split())
graph = [list() for _ in range(N + 1)]
for _ in range(M):
    f_node, s_node = map(int, read().split())
    graph[f_node].append(s_node)
    graph[s_node].append(f_node)

visited = [False] * (N + 1)

def bfs(started):
    visited[started] = True
    queue = deque([started])
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True

# 1부터 N까지의 정점을 모두 순회한다.
count = 0
for i in range(1, N + 1):
    # 아직 방문하지 않은 노드가 있다면, 해당 노드와 인접한 모든 노드를
    # bfs 탐색 알고리즘을 통해 전부 방문하고, 연결 요소 수량을 추가한다.
    if not visited[i]:
        bfs(i)
        count += 1
print(count)