import sys
from collections import deque

read = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
field = [list(read().strip()) for _ in range(12)]

# 필드의 가로, 세로 값을 담은 변수 N, M
N, M = 12, 6

def remove_puyo(y, x, color):
    queue = deque([(y, x)])
    puyos = [(y, x)]
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my, mx = ny + direct[0], nx + direct[1]
            if 0 <= my < N and 0 <= mx < M:
                if field[my][mx] == color and (my, mx) not in puyos:
                    queue.append((my, mx))
                    puyos.append((my, mx))

    # 만약 인접한 동일 색상 뿌요가 4개 이상이라면, 이를 제거함.
    if len(puyos) >= 4:
        for ly, lx in puyos:
            field[ly][lx] = '.'
        return True

    return False


# 뿌요 밑에 빈 공간이 있을 경우, 뿌요를 아래로 내리는 방법.
def set_field():
    # 10 줄부터 0 줄까지, 역순으로 빈 공간이 있는지를 탐색함.
    for ly in range(N - 2, -1, -1):
        for lx in range(M):
            if field[ly][lx] != '.':
                down = 1
                # 바로 아랫줄이 유효 구역 내에 있고, 빈 공간이라면 위치 변경.
                while ly + down < N and field[ly + down][lx] == '.':
                    # 바로 아랫줄에 위치한 빈 공간과 현재 뿌요의 위치를 바꾸는 수식.
                    field[ly + down][lx], field[ly + down - 1][lx] = field[ly + down - 1][lx], field[ly + down][lx]
                    down += 1


# 필드를 순회하면서, 제거가 가능한 뿌요 덩어리가 있는지를 판별하는 함수.
def find_puyo():
    can_combo = False
    for i in range(N):
        for j in range(M):
            if field[i][j] == '.':
                continue
            if remove_puyo(i, j, field[i][j]):
                can_combo = True

    return can_combo


combo = 0
while True:
    # 제거 가능한 뿌요 덩어리가 있는지를 판별.
    if not find_puyo():
        break
    set_field()
    combo += 1
print(combo)