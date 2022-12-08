# 게임 종료 조건, 머리가 벽에 부딪히거나 몸에 부딪히는 순간 종료.


import sys

read = sys.stdin.readline
N, K = int(read()), int(read())
# 좌표의 값은 1부터 시작이기 때문에 이를 맞춰주기 위해서 0부터 시작하도록 1을 감산.
apples = [tuple(map(lambda x: int(x) - 1, read().split())) for _ in range(K)]

L = int(read())
controls = []
for _ in range(L):
    time, dir = read().split()
    controls.append((int(time), -1 if dir == "L" else 1))

# 순서대로 동, 남, 서, 북 방향에 대한 2차원 벡터 (y, x) => (시계 방향 : + 1, 반시계 방향 : - 1)
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_kr = ['동', '남', '서', '북']
snack_body = [(0, 0)]

head_loc = [(0, 0)]
current_time = 0
look_direction = 0 # 오른쪽, 즉 동쪽을 바라보며 시작.
while head_loc:
    current_time += 1
    # 바라보는 방향에 대한 y, x 변화 값을 가져와 더해줌.
    ny, nx = head_loc.pop()
    look_y, look_x = direction[look_direction]
    my, mx = ny + look_y, nx + look_x

    # 가는 길에 사과가 있다면, 해당 좌표까지 몸을 늘인 것.
    if (my, mx) in apples:
        apples.remove((my, mx))
        snack_body.append((my, mx))
        head_loc.append((my, mx))
    # 가는 길에 사과는 없지만, 벽과 몸에 부딪히지 않은 경우 꼬리를 줄인다.
    elif 0 <= my < N and 0 <= mx < N and (my, mx) not in snack_body:
        snack_body.append((my, mx))
        del snack_body[0]
        head_loc.append((my, mx))
    # 그 외의 경우 게임을 종료 시킨다.
    else:
        break

    # 이동을 진행한 후후에, 뱀이 바보는 방향을 변경해야 하는지 체크.
    # 또한 입력 받은 명령을 모두 수행하였는지도 체크해야 함.
    if controls:
        oper_time, oper_dir = controls[0]
        if current_time == oper_time:
            look_direction = (look_direction + oper_dir) % 4
            del controls[0]

print(current_time)