import sys
from collections import deque

read = sys.stdin.readline
N = int(read())
tree = [list() for _ in range(N)]
root = 0

for i, value in enumerate(map(int, read().split())):
    if value != -1:
        tree[value].append(i)
    else:
        root = i


def get_removed(removed):
    removed_node = [False] * N
    queue = deque([removed])
    while queue:
        rm_node = queue.popleft()
        # 해당 노드를 제거 대상인 노드로 설정함.
        removed_node[rm_node] = True
        # 해당 노드가 자식 노드를 가지고 있는지를 판별.
        if tree[rm_node]:
            # 자식 노드도 제거 대상이므로 덱에 목록을 추가.
            for child_node in tree[rm_node]:
                queue.append(child_node)

    return removed_node

# 제거 대상인 노드를 제외한 나머지 트리 중에서, 단말 노드의 수량을 계산
def bfs(node, removed_list):
    leaf_node = 0
    visited = [False] * N
    visited[node] = True
    queue = deque([node])
    while queue:
        current_node = queue.popleft()
        # 탐색한 노드가 제거 대상인지를 먼저 판별해야 함.
        if removed_list[current_node]:
            continue
        # 해당 노드의 자식 노드 중에서, 삭제 예정인 노드를 제외함.
        child_nodes = tree[current_node]
        for cd_node in child_nodes:
            if removed_list[cd_node]:
                child_nodes.remove(cd_node)
        # 그 후 남은 자식 노드가 0이라면, 단말 노드이므로 카운트 1 추가.
        if len(child_nodes) == 0:
            leaf_node += 1
            continue

        # 남은 자식 노드가 존재한다면, 덱에 목록을 추가해야 함.
        for child_node in child_nodes:
            # 해당 노드를 아직 방문하지 않았다면, 방문 처리를 진행함.
            if not visited[child_node]:
                visited[child_node] = True
                queue.append(child_node)
    return leaf_node


removed_list = get_removed(int(read()))
result = bfs(root, removed_list)
print(result)
