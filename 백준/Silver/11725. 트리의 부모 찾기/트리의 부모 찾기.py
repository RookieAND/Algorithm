import sys
from collections import deque

read = sys.stdin.readline
N = int(read())

visited = [False] * (N + 1)
parent = [-1] * (N + 1)

tree = [list() for _ in range(N + 1)]
for i in range(N-1):
    f_node, s_node = map(int, read().split())
    tree[f_node].append(s_node)
    tree[s_node].append(f_node)


def bfs(node):
    queue = deque([node])
    while queue:
        # 해당 노드의 자식 노드 목록을 먼저 불러온다.
        child_node = queue.popleft()
        # 자식 노드들을 하나씩 순회하면서, 방문 여부를 판별한다.
        for cd_node in tree[child_node]:
            if not visited[cd_node]:
                # 방문을 하지 않았다면, 부모 노드 정보를 추가하고 방문 처리한다.
                visited[child_node] = True
                parent[cd_node] = child_node
                queue.append(cd_node)

bfs(1)
print(*parent[2:], sep='\n')
