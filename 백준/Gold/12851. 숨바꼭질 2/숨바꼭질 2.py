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
        if 0 <= k_time < cur_time:
            break
        for loc in [current - 1, current + 1, current * 2]:
            if 0 <= loc <= 100000:
                loc_time, loc_case = visited[loc]
                if loc_time == -1:
                    visited[loc] = (cur_time + 1, 1)
                    queue.append(loc)
                elif cur_time + 1 < loc_time:
                    visited[loc] = (cur_time + 1, 1)
                    queue.append(loc)
                elif cur_time + 1 == loc_time:
                    visited[loc] = (loc_time, loc_case + 1)
                    queue.append(loc)
    return visited[K]

result = bfs(N)
print(result[0], result[1], sep='\n')