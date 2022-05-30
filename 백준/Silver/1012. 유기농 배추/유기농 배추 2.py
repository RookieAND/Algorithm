import sys
sys.setrecursionlimit(10 ** 5)

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# 인접한 1을 전부 0으로 변경하는 dfs 함수를 정의한다.
# 단, 2차원 배열에서 첫 번째 인덱스는 y, 두 번째 인덱스는 x 임을 유의.
def dfs(y, x):
    graph[y][x] = 0
    # 현재 위치를 기준으로, 네 방향에 대한 탐색을 진행한다.
    for direct in direction:
        ny = y + direct[0]
        nx = x + direct[1]
        # 만약 인접한 노드에 1이 있다면, 이에 대한 dfs 재귀를 진행한다.
        if (0 <= ny < n and 0 <= nx < m) and graph[ny][nx]:
            dfs(ny, nx)


read = sys.stdin.readline
t = int(read())
for _ in range(t):
    m, n, k = map(int, read().split())
    graph = [[0] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, read().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                dfs(i, j)
                count += 1
    print(count)
