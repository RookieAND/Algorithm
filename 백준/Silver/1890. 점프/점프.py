import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
matrix = [list(map(int, read().split())) for _ in range(N)]
# dp[i][j] = i, j 칸까지 올 수 있는 가장 적은 경로의 수
dp = [[0] * N for _ in range(N)]
# 시작 지점의 경로는 1개, 이를 초기화 해줌
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        move = matrix[i][j]
        # 우측 하단 (도착 지점) 에 도착했을 경우, 값 출력
        if i == N - 1 and j == N - 1:
            print(dp[N - 1][N - 1])
            sys.exit(0)
        # 오른쪽으로 이동할 수 있는 경우
        if j + matrix[i][j] < N:
            dp[i][j + move] += dp[i][j]
        # 아래쪽으로 이동할 수 있는 경우
        if i + matrix[i][j] < N:
            dp[i + move][j] += dp[i][j]