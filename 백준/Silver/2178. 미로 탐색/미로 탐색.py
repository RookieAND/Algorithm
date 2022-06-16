# 현재 위치한 칸에 "해당 칸까지 이동하기 위해 지나야 하는 칸 수" 를 저장한다.
# BFS 탐색을 통해 상하좌우를 파악한 후, 지나갈 수 있는 길이 있다면 탐색 범위에 추가.
import sys
from collections import deque

read = sys.stdin.readline
N, M = map(int, read().split())
# 문자열로 읽어들인 목록을 map 함수로 분해해야 함.
maze = [list(map(int, read().strip())) for _ in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# bfs 탐색을 통해 경로 탐색 시작.
def bfs(y, x):
    queue = deque([(y, x)])
    while queue:
        ny, nx = queue.popleft()
        for direct in direction:
            my, mx = ny + direct[0], nx + direct[1]
            # 유효한 탐색 범위 이내이면서, 아직 이동하지 않은 길목인지 탐색.
            if (0 <= my < N and 0 <= mx < M) and maze[my][mx] == 1:
                maze[my][mx] = maze[ny][nx] + 1
                queue.append((my, mx))

bfs(0, 0)
print(maze[N-1][M-1])