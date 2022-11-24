import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001

def bfs(start):
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == K:
            return visited[K]
        # 현재 좌표의 -1, +1, x2 만큼 위치한 좌표들을 대상으로 탐색.
        for loc in [current - 1, current + 1, current * 2]:
            # 해당 좌표가 유효 범위 안에 있으면서, 미방문된 상태인지 체크.
            if 0 <= loc <= 100000 and not visited[loc]:
                visited[loc] = visited[current] + 1
                queue.append(loc)

print(bfs(N))