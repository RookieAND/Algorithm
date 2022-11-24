import sys
from collections import deque

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
read = sys.stdin.readline

N, M = map(int, read().split())
matrix = [list(map(int, read().rstrip())) for _ in range(N)]

def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    queue = deque([(0, 0, 0)])
    while queue:
        y, x, wall = queue.popleft()
        # 탐색 끝에 도착 지점에 도달했을 경우, 값을 리턴한다.
        if y == N - 1 and x == M - 1:
            return visited[y][x][wall] + 1

        for direct in direction:
            ny, nx = y + direct[0], x + direct[1]
            # 다음 이동 좌표가 미방문 지역이며, 유효 범위 내에 있는지를 체크해야 함.
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx][wall]:
                # 다음 이동 경로가 벽이 아니라면, 그대로 이동한다.
                if not matrix[ny][nx]:
                    queue.append((ny, nx, wall))
                    visited[ny][nx][wall] = visited[y][x][wall] + 1
                    continue
                # 만약 다음 이동 경로가 벽이고, 파괴 횟수가 0이라면 벽을 부순다.
                if wall == 0:
                    queue.append((ny, nx, 1))
                    visited[ny][nx][1] = visited[y][x][wall] + 1

    return -1

print(bfs())