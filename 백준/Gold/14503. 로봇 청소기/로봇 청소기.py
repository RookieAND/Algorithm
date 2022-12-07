import sys
from collections import deque

# 4방향에 대한 2차원 벡터 선언 (0은 북쪽, 1은 동쪽, 2는 남쪽, 3은 서쪽)
# 이동에 대한 구현을 쉽게 조율하기 위해 같은 내용을 한번 더 반복.
direction = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 0), (0, 1), (1, 0), (0, -1)]

read = sys.stdin.readline
N, M = map(int, read().split())
R, C, D = map(int, read().split())

matrix = [list(map(int, read().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

cleaning = 0
# 현재 로봇이 바라보는 방향을 담은 값 (direction의 4번째 인덱스부터 활용 예정)
current_direction = D + 4
# queue 에는 청소가 가능한 좌표를 담아둘 예정.
# R, C 좌표는 1부터 시작이기 때문에 이를 제해야 함.
next_loc = [(R, C)]
while next_loc:
    ny, nx = next_loc.pop()
    # 후진을 통해 되돌아온 경우도 있기 때문에, 이를 체크해야 함.
    cleaning += 1 if not visited[ny][nx] else 0
    visited[ny][nx] = True
    # direction 배열에서 인덱스 - 1의 의미는 좌측으로 회전했다는 의미.
    # -1 ~ -4 (좌측 회전을 총 4번) 의 값을 순차적으로 대입하면서 청소가 가능한지를 판별.
    is_rotate = False
    for rotate in range(1, 5):
        rotate_direction = current_direction - rotate
        my, mx = ny + direction[rotate_direction][0], nx + direction[rotate_direction][1]
        # 회전울 마치고 바라본 장소가 청소가 가능한지를 판별해야 함
        # 만약 청소가 가능하다면 해당 장소를 방문 처리하고, 해당 장소로 로봇을 이동시킴
        if 0 <= my < N and 0 <= mx < M:
            if not visited[my][mx] and not matrix[my][mx]:
                # 회전된 방향에 대한 값을 업데이트 해야 함.
                # 만약 인덱스 값이 4보다 작다면 이를 보충하기 위해 4를 더해줌.
                current_direction -= rotate
                current_direction += 4 if current_direction < 4 else 0
                next_loc.append((my, mx))
                # 이미 로봇이 이동했으므로 더 이상 회전을 고려하지 않아도 됨.
                is_rotate = True
                break
    # 네 방향 모두 청소가 되어 있거나 벽이 있어 이동을 하지 못한 경우. 후진을 진행.
    if not is_rotate:
        by, bx = ny - direction[current_direction][0], nx - direction[current_direction][1]
        # 후진한 위치에 벽이 있는지, 유효한 공간인지를 판별해야 함
        if 0 <= by < N and 0 <= bx < M and not matrix[by][bx]:
            next_loc.append((by, bx))
        # 후진도 못할 경우 작동을 멈춰야 함.
        else:
            break

print(cleaning)