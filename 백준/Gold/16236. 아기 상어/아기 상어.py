import sys
from collections import deque

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

read = sys.stdin.readline
N = int(read())

# shark_loc은 현재 아기 상어가 위치한 좌표 (y, x) 의 정보
# shark_size 는 현재 아기 상어의 크기 (2부터 시작)
shark_loc, shark_size, eaten_fish = (0, 0), 2, 0

# matrix 는 현재 물고기와 상어가 놓인 공간을 담는 이차원 배열
# fishes 는 각 물고기의 위치와 크기 (y, x, size) 에 대한 정보를 담은 배열
matrix, fishes = [], []

for row in range(N):
    matrix.append(list(map(int, read().split())))
    for col in range(N):
        # 아기 상어가 위치한 칸일 경우 저장
        if matrix[row][col] == 9:
            shark_loc = (row, col)
        # 물고기가 놓인 칸일 경우 저장
        elif 0 < matrix[row][col] <= 6:
            fishes.append([row, col, matrix[row][col]])

# 아기 상어가 먹이를 모두 먹기까지 걸린 시간 time
time = 0
while fishes:

    # 먼저, 아기 상어가 이동 가능한 공간을 모두 이동했을 경우, 각 좌표에 대한 이동 거리를 구해야 함.
    shark_y, shark_x = shark_loc
    distances = [[-1] * N for _ in range(N)]
    distances[shark_y][shark_x] = 0

    queue = deque([(shark_y, shark_x)])
    while queue:
        ny, nx = queue.popleft()
        for dy, dx in direction:
            my, mx = ny + dy, nx + dx
            # 유효 범위 내로 이동 가능하면서, 이동이 가능한 칸인지를 조사해야 함
            if 0 <= my < N and 0 <= mx < N and matrix[my][mx] <= shark_size:
                # 해당 칸이 아직 한번도 이동하지 않은 칸인지, 이동을 했을 때 거리가 줄어드는지를 조사.
                if distances[my][mx] == -1 or distances[my][mx] > distances[ny][nx] + 1:
                    distances[my][mx] = distances[ny][nx] + 1
                    queue.append((my, mx))

    # 모든 물고기를 순화하면서, 아기 상어가 먹을 수 있는 생선 중 가장 가까운 거리에 위치한 것을 고르기.
    eat_fish_idx, eat_fish_dist = None, 10e6
    for idx in range(len(fishes)):
        fy, fx, size = fishes[idx]
        # 현재 거리가 기존의 거리보다 짧고, 사이즈 또한 아기 상어가 먹을 수 있다면 새롭게 업데이트.
        if 0 < distances[fy][fx] < eat_fish_dist and size < shark_size:
            eat_fish_idx = idx
            eat_fish_dist = distances[fy][fx]

    # 만약 먹을 수 있는 물고기가 없다면 탐색 종료.
    if eat_fish_idx is None:
        break

    # 아기 상어가 물고기를 먹기 위해 이동한 거리만큼 시간 증가
    time += eat_fish_dist

    # 그렇지 않을 경우, 가장 가까운 위치에 놓인 물고기를 향해 이동.
    shark_y, shark_x = shark_loc
    eat_fish_y, eat_fish_x = fishes[eat_fish_idx][:2]

    # 상어의 위치와 먹은 물고기에 대한 정보를 업데이트 함.
    shark_loc = (eat_fish_y, eat_fish_x)
    matrix[shark_y][shark_x] = 0
    matrix[eat_fish_y][eat_fish_x] = 9

    eaten_fish += 1
    # 아기 상어가 자신의 몸집만큼 물고기를 섭취했다면, 크기를 1 증가시킴.
    if eaten_fish == shark_size:
        eaten_fish = 0
        shark_size += 1

    # 먹은 물고기를 물고기 목록에서 제거
    del fishes[eat_fish_idx]

print(time)