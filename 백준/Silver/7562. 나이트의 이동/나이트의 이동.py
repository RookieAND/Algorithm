import sys
from collections import deque

read = sys.stdin.readline
N = int(read())

direction = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for _ in range(N):
    L = int(read())
    matrix = [[0] * L for _ in range(L)]
    current_x, current_y = map(int, read().split())
    goal_x, goal_y = map(int, read().split())

    matrix[current_y][current_x] = 1
    queue = deque([(current_y, current_x)])
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my, mx = ny + direct[0], nx + direct[1]
            if (0 <= my < L and 0 <= mx < L) and matrix[my][mx] == 0:
                queue.append((my, mx))
                matrix[my][mx] = matrix[ny][nx] + 1

    print(matrix[goal_y][goal_x] - 1, sep='\n')