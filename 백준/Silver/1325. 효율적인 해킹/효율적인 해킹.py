import sys
from collections import deque

read = sys.stdin.readline
N, M = map(int, read().split())
graph = [list() for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, read().split())
    graph[b].append(a)

# BFS 탐색 알고리즘을 통해, 상위 노드와 연결된 하위 노드를 모두 찾음
# 만약 노드를 탐색할 경우 방문 처리를 하고, 컴퓨터 수량에 1을 추가함.
def bfs(start):
    visited = [False] * (N + 1)
    visited[start] = True
    hacked, queue = 0, deque([start])
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                hacked += 1
    return hacked


# 모든 컴퓨터를 대상으로 최대 해킹 가능한 수량을 체크.
result, is_hacked = [], 0
for i in range(1, N + 1):
    can_hacked = bfs(i)
    # 만약 더 많은 컴퓨터를 해킹할 수 있는 노드가 나온다면,
    # 기존에 저장했던 목록을 초기화하고 새롭게 목록을 할당.
    if is_hacked < can_hacked:
        is_hacked = can_hacked
        result = [i]
    # 최댓값과 같은 수량의 컴퓨터를 해킹할 수 있다면 목록에 추가함.
    elif is_hacked == can_hacked:
        result.append(i)

# 오름차순으로 나열하여 정답 출력
print(*sorted(result))
