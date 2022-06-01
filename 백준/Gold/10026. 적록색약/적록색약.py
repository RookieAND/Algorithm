import copy
import sys
from collections import deque

read = sys.stdin.readline
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N = int(read())
picture = [list(read().strip()) for _ in range(N)]
picture_rg = copy.deepcopy(picture)
rgb = ['R', 'G', 'B']


# 같은 색상을 찾고, 전부 찾았다면 하얀색 (W) 으로 칠한다고 가정.
def bfs(y, x):
    color = picture[y][x]
    picture[y][x] = "W"
    queue = deque([(y, x)])
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my = ny + direct[0]
            mx = nx + direct[1]
            if (0 <= my < N and 0 <= mx < N) and picture[my][mx] == color:
                queue.append((my, mx))
                picture[my][mx] = "W"


def bfs_rg(y, x):
    color = picture_rg[y][x]
    picture_rg[y][x] = "W"
    queue = deque([(y, x)])
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my = ny + direct[0]
            mx = nx + direct[1]
            if 0 <= my < N and 0 <= mx < N:
                if color == 'B':
                    if picture_rg[my][mx] == 'B':
                        queue.append((my, mx))
                        picture_rg[my][mx] = 'W'
                    continue
                # 선택된 색상이 R, G일 때, 이동된 색상이 B가 아니라면 해당.
                if picture_rg[my][mx] in ['R', 'G']:
                    queue.append((my, mx))
                    picture_rg[my][mx] = 'W'


amount = amount_rg = 0
for i in range(N):
    for j in range(N):
        color_rg = picture_rg[i][j]
        color_normal = picture[i][j]
        if color_normal != 'W':
            bfs(i, j)
            amount += 1
        if color_rg != 'W':
            bfs_rg(i, j)
            amount_rg += 1

print(amount, amount_rg)
