import sys
from collections import deque

# 그래프가 이동할 수 있는 방향 벡터를 list에 저장한다. (y, x)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 인접한 1을 전부 0으로 변경하는 bfs 함수를 정의한다.
# 단, 2차원 배열에서 첫 번째 인덱스는 y, 두 번째 인덱스는 x 임을 유의.
def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        current_loc = queue.popleft()
        # 현재 위치를 기준으로 네 방향에 대한 탐색을 진행한다.
        for direct in directions:
            ny = current_loc[0] + direct[0]
            nx = current_loc[1] + direct[1]
            # 만약 인접한 노드에 1이 있다면, 이 또한 0으로 변경하고 큐에 좌표를 추가한다.
            if (0 <= nx < m and 0 <= ny < n) and graph[ny][nx]:
                graph[ny][nx] = 0
                queue.append((ny, nx))


# readline을 활용할 수 있는 방안, 앞으로는 이렇게 작성해보자.
read = sys.stdin.readline
t = int(read())
for _ in range(t):
    m, n, k = map(int, read().split())
    graph = [[0] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        # x, y인 이유는 첫번째로 가로줄에 대한 좌표를 받기 때문이다.
        x, y = map(int, read().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                graph[i][j] = 0
                bfs(i, j)
                count += 1

    print(count)
