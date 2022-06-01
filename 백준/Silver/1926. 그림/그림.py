import sys
from collections import deque


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

read = sys.stdin.readline
N, M = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]
amount = size = 0


def bfs(y, x):
    queue = deque([(y, x)])
    picture_size = 1
    graph[y][x] = 0
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my = ny + direct[0]
            mx = nx + direct[1]
            if (0 <= my < N and 0 <= mx < M) and graph[my][mx]:
                picture_size += 1
                queue.append((my, mx))
                graph[my][mx] = 0

    return picture_size

for i in range(N):
    for j in range(M):
        # 그림을 찾았다면, 수량을 증가시키고 주변에 위치한 1을 0으로 제거.
        # 그 과정에서 찾은 1의 수량 (그림의 크기) 를 리턴하여 별도로 저장.
        if graph[i][j]:
            pic_size = bfs(i, j)
            # 새롭게 찾은 그림의 사이즈가 기존보다 크다면 업데이트 진행.
            size = pic_size if pic_size > size else size
            amount += 1

print(amount, size, sep='\n')
