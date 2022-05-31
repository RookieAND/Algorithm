import sys
from collections import deque

read = sys.stdin.readline
N, M, K = map(int, read().split())
result = 0
# 음식물이 떨어졌다면 1, 없다면 0이라 가정하고 이차원 배열 생성
graph = [[0] * (M) for _ in range(N)]

# 좌표가 1부터 시작하므로 x, y 값에 1을 제외해야 함.
for _ in range(K):
    y, x = map(int, read().split())
    graph[y-1][x-1] = 1

# 각각 북, 남, 동, 서 방향을 나타내는 2차원 벡터를 지정
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# 인접한 1의 갯수를 size에 저장하여 리턴하는 bfs 함수 선언.
def bfs(y, x):
    queue = deque([(y, x)])
    size = 1
    while queue:
        y, x = queue.popleft()
        for direct in direction:
            ny = y + direct[0]
            nx = x + direct[1]
            # 만약 4방향 중 인접한 곳에 1이 추가로 있는지를 판별
            if (0 <= ny < N and 0 <= nx < M) and graph[ny][nx]:
                queue.append((ny, nx))
                # 1이 존재한다면, 값을 0으로 바꾸고 크기 1 증가.
                graph[ny][nx] = 0
                size += 1
    return size

for i in range(N):
    for j in range(M):
        if graph[i][j]:
            graph[i][j] = 0
            size = bfs(i, j)
            # 만약 새롭게 얻은 크기가 기존보다 크다면 업데이트.
            result = size if size > result else result

print(result)