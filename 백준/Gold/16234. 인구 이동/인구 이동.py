# 그래프를 순회하며 인접한 나라가 L명 이상 R명 이하의 인구 차이를 보이는 경우 연합 목록에 추가한다.
# 순회를 완료한 후, 연합 목록에 추가된 모든 나라의 값을 (연합의 인구수) / (칸의 개수) 로 설정한다.
# 다른 곳에서 연합이 또 발생하였을 경우, 이 또한 체크하여 조사한다.

import sys
from collections import deque

read = sys.stdin.readline
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, L, R = map(int, read().split())
land = [list(map(int, read().split()))for _ in range(N)]


def is_union(start_y, start_x):
    global visited
    queue = deque([(start_y, start_x)])
    union = [(start_y, start_x)]
    while queue:
        ny, nx = queue.popleft()
        for dy, dx in direction:
            my, mx = ny + dy, nx + dx
            if 0 <= my < N and 0 <= mx < N and not visited[my][mx]:
                if L <= abs(land[ny][nx] - land[my][mx]) <= R:
                    queue.append((my, mx))
                    union.append((my, mx))
                    visited[my][mx] = True

    if len(union) == 1:
        return False
    union_avg = sum([land[uy][ux] for uy, ux in union]) // len(union)
    for uy, ux in union:
        land[uy][ux] = union_avg
    return True

result = 0
while True:
    is_open = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                if is_union(i, j):
                    is_open = True
    if not is_open:
        break
    result += 1
print(result)