import sys
from collections import deque

# 이동이 가능한 여덟 방향에 대한 2차원 벡터 값을 list로 저장해둔다.
direction = [(1, 0), (-1, 0), (0, 1), (0, -1),
             (-1, -1), (-1, 1), (1, -1), (1, 1)]


# BFS 탐색 알고리즘을 통해 인접한 섬을 전부 소거하는 방식으로 진행.
# 인접한 8방향에 위치한 노드를 탐색하여, 값이 1이라면 전부 0으로 변환
def bfs(y, x):
    queue = deque([(y, x)])
    graph[y][x] = 0
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my = ny + direct[0]
            mx = nx + direct[1]
            if (0 <= my < H and 0 <= mx < W) and graph[my][mx]:
                queue.append((my, mx))
                graph[my][mx] = 0


read = sys.stdin.readline
result = []
while True:
    W, H = map(int, read().split())
    # 만약 입력 받은 W, H 값이 둘 다 0일 경우 무한 루프 종료.
    if not W and not H:
        break
    # 그렇지 않을 경우, 입력된 테스트 케이스를 토대로 그래프 도식화.
    graph = [list(map(int, read().split())) for _ in range(H)]

    island = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j]:
                bfs(i, j)
                island += 1
    result.append(island)

print(*result, sep='\n')