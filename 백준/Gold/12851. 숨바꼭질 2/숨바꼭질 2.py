# visited 배열 내부의 값을 tuple 로 지정한다.
# visited[i] = (a, b) 는, i 좌표에 도달하기까지 a 초가 걸리며 b 개의 방식이 존재한다는 의미다.
# 너비 탐색을 통해 특정 위치에 도달했을 경우, 3개의 케이스를 고려한다.
# 1. i 까지 도달한 시간이 기존의 시간 (a) 보다 값이 적을 경우.
#   => 이를 새로운 값으로 초기화 한다.
# 2. i 까지 도달한 시간이 기존의 시간 (a) 와 같을 경우.
#   => 방법이 하나 추가된 것이므로 b + 1을 한다.
# 3. i 까지 도달한 시간이 기존의 시간보다 클 경우.
#   => 최적의 결과를 찾을 수 없으므로 탐색을 종료해야 한다.

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [(-1, 0)] * 100001

def bfs(start):
    queue = deque([start])
    visited[start] = (0, 1)
    while queue:
        current = queue.popleft()
        cur_time, cur_case = visited[current]
        k_time, k_case = visited[K]
        # K 까지 이동하는데 소요되는 시간이 현재 이동시간보다 큰지를 확인. (시간이 더 크면 더 이상 반복하는 게 무의미함)
        # K 좌표를 한번도 방문하지 않았을 경우는 해당 조건을 무시해야 함.
        if 0 <= k_time < cur_time:
            break
        # 현재 좌표의 -1, +1, x2 만큼 위치한 좌표들을 대상으로 탐색.
        for loc in [current - 1, current + 1, current * 2]:
            # 해당 좌표가 유효 범위 안에 있는지를 먼저 체크.
            if 0 <= loc <= 100000:
                loc_time, loc_case = visited[loc]
                # 아직 해당 좌표를 방문하지 않았을 경우, 시간과 방법 초기화
                if loc_time == -1:
                    visited[loc] = (cur_time + 1, 1)
                    queue.append(loc)
                # 만약 현재 이동 시간이 기존의 소요 시간보다 작을 경우, 업데이트
                elif cur_time + 1 < loc_time:
                    visited[loc] = (cur_time + 1, 1)
                    queue.append(loc)
                # 만약 현재 이동 시간이 기존의 소요 시간과 같다면, 방법 추가
                elif cur_time + 1 == loc_time:
                    visited[loc] = (loc_time, loc_case + 1)
                    queue.append(loc)
    # 만약 반복이 종료되었다면 visited[K] 리턴
    return visited[K]

result = bfs(N)
print(result[0], result[1], sep='\n')