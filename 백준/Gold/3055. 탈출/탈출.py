import sys
from collections import deque

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
read = sys.stdin.readline
R, C = map(int, read().split())

goal_y, goal_x = 0, 0
queue = deque()
matrix = []
distance = [[0] * C for _ in range(R)]

for row in range(R):
    matrix.append(list(read().rstrip()))
    for col in range(C):
        if matrix[row][col] == 'D':
            goal_y, goal_x = (row, col)
        # 항상 고슴도치가 먼저 이동하는 것을 가정하기에, appendleft 진행.
        elif matrix[row][col] == 'S':
            queue.appendleft((row, col))
        elif matrix[row][col] == "*":
            queue.append((row, col))

def bfs():
    while queue:
        if matrix[goal_y][goal_x] == "S":
            return distance[goal_y][goal_x]
        ny, nx = queue.popleft()
        for dy, dx in direction:
            my, mx = ny + dy, nx + dx
            # 다음으로 이동할 수 있는 공간은 돌과 물을 제외한 나머지.
            if 0 <= my < R and 0 <= mx < C:
                # 고슴도치가 이동 가능한 공간은 빈 공간 혹은 비버의 굴이다.
                if matrix[ny][nx] == "S" and (matrix[my][mx] == "." or matrix[my][mx] == "D"):
                    matrix[my][mx] = "S"
                    distance[my][mx] = distance[ny][nx] + 1
                    queue.append((my, mx))
                # 물이 차오를 수 있는 공간은 빈 공간 혹은 고슴도치가 서 있던 공간이다.
                elif matrix[ny][nx] == "*" and (matrix[my][mx] == "." or matrix[my][mx] == "S"):
                    matrix[my][mx] = "*"
                    queue.append((my, mx))
    return 'KAKTUS'

print(bfs())