import sys
from collections import deque

read = sys.stdin.readline
M, N= map(int, read().split())

# 토마토가 익을 수 있는 방향에 대한 2차원 벡터 4가지를 List에 저장하여 보관.
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

tomato_box = []
tomato_loc = deque()
not_ripped = 0

for row in range(N):
    tomato_row = list(map(int, read().split()))
    tomato_box.append(tomato_row)
    # 덜 익은 토마토의 수량을 변수에 추가함.
    not_ripped += tomato_row.count(0)
    for col in range(len(tomato_row)):
        # 토마토가 들어있는 상자의 좌표를 loc에 추가함.
        if tomato_row[col] == 1:
            tomato_loc.append((row, col))

# 만약 상자에 담긴 토마토가 전부 익었다면, 0을 출력시키고 종료
if not_ripped == 0:
    print(0)
    sys.exit(0)

while tomato_loc:
    ny, nx = tomato_loc.popleft()
    for direct in direction:
        my = ny + direct[0]
        mx = nx + direct[1]
        if (0 <= my < N and 0 <= mx < M) and tomato_box[my][mx] == 0:
            tomato_loc.append((my, mx))
            tomato_box[my][mx] = tomato_box[ny][nx] + 1

result = 0
for tomato_row in tomato_box:
    for day in tomato_row:
        # 만약 아직도 익지 않은 토마토가 존재한다면, -1을 출력시켜야 함.
        if day == 0:
            print(-1)
            sys.exit(0)
        # 그렇지 않을 경우, 최댓값을 산출하여 새로이 result 변수를 업데이트.
        result = max(day, result)

# 시작은 0일차부터이므로, 기존의 값에서 1을 제외한 값이 정답이 됨.
print(result - 1)