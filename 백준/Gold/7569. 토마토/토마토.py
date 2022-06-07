import sys
from collections import deque

read = sys.stdin.readline
M, N, H = map(int, read().split())

# 토마토가 익을 수 있는 방향에 대한 3차원 벡터 6가지를 List에 저장하여 보관.
direction = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

# 토마토 박스가 H 층 별로 담긴 것을 3차원 배열로 담아 표현하였음.
tomato_boxes = [[list(map(int, read().split())) for _ in range(N)] for _ in range(H)]

# 토마토만 담긴 좌표를 따로 모아 덱에 보관하는 과정
tomato_list = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            # 만약 토마토가 든 좌표를 찾았다면, 이를 목록에 추가하기
            if tomato_boxes[z][y][x] == 1:
                tomato_list.append((z, y, x))

# 전달 받은 박스에 든 토마토가 전부 익었는지를 파악하기 위해, 덜 익은 토마토 수량을 셈.
not_ripped_tomato = 0
for tomato_box in tomato_boxes:
    for tomato_row in tomato_box:
        not_ripped_tomato += tomato_row.count(0)
# 만약 덜 익은 토마토가 하나도 없다면, 그 즉시 0을 출력시키고 구문 종료
if not_ripped_tomato == 0:
    print(0)
    sys.exit(0)

# 보관된 토마토 좌표를 큐에 모두 추가하고, 총 몇 번의 반복이 진행되는지를 판별해야 함.
# 시작은 0일차이므로, while 문에서 day에 1을 추가하는 것을 고려하여 -1부터 시작.
day = -1
while tomato_list:
    # 그날 익은 토마토의 수량만큼만 반복문을 진행시켜야 함. (하루에 한 칸씩 익으므로)
    # 따라서 현재 queue에 담긴 토마토가 당일 인접한 다른 토마토들을 전부 익게끔 만듬.
    tomato_amount = len(tomato_list)
    day += 1
    for _ in range(tomato_amount):
        nz, ny, nx = tomato_list.popleft()
        for direct in direction:
            mz = nz + direct[0]
            my = ny + direct[1]
            mx = nx + direct[2]
            if (0 <= mz < H and 0 <= my < N and 0 <= mx < M) and tomato_boxes[mz][my][mx] == 0:
                tomato_list.append((mz, my, mx))
                tomato_boxes[mz][my][mx] = 1

# 토마토가 전부 다 익고 나서, 덜 익은 토마토가 있는지 파악해야 함.
for tomato_box in tomato_boxes:
    for tomato_row in tomato_box:
        # 만약 해당 열에 0이 있다면, 그 즉시 -1을 출력시키고 구문 종료
        if tomato_row.count(0) > 0:
            print(-1)
            sys.exit(0)

print(day)
