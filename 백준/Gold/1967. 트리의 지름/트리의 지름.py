import sys
from collections import deque

read = sys.stdin.readline
N = int(read())
tree = [list() for _ in range(N + 1)]

# 각 간선의 가중치와 부모 - 자식 노드를 연결시켜 tree에 추가함.
for _ in range(N-1):
    p_node, c_node, dist = map(int, read().split())
    tree[p_node].append((c_node, dist))
    tree[c_node].append((p_node, dist))


# 루트 노드로부터 가장 거리가 먼 노드와, 거리를 구하는 함수를 작성.
# 해당 노드와 이어진 노드들의 목록을 덱에 추가하여 순회
def bfs(node):
    farest_node, distance = 0, 0
    queue = deque(tree[node])
    visited = [False] * (N + 1)
    visited[node] = True
    while queue:
        nd, dist = queue.popleft()
        visited[nd] = True
        # 만약 더 거리가 먼 노드를 찾았다면, 이를 업데이트 해야 함.
        if dist > distance:
            farest_node = nd
            distance = dist
        # 해당 노드까지의 거리에서 추가 가중치만큼을 더하여 덱에 추가.
        for new_nd, new_dist in tree[nd]:
            if not visited[new_nd]:
                queue.append((new_nd, dist + new_dist))
    return farest_node, distance

# 루트 노드로부터 가장 먼 노드만을 선별하여 구한다.
far_node, _ = bfs(1)
# 그 후, 가장 먼 노드로부터 가장 먼 노드와의 거리를 구한다.
_, radius = bfs(far_node)
print(radius)