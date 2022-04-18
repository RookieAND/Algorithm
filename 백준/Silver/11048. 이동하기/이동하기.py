import sys

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * M for i in range(N)]

# 가장 첫번째 열에 놓인 값을 초기화 시켜야 함 (아래로 내려갈 수록 사탕 수량 합산)
dp[0][0] = maze[0][0]

# 가장 첫번째 열에 놓인 값들의 dp 점화식 = dp[i][0] = dp[i-1][0] + maze[i][0]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + maze[i][0]

# 두 번째 열부터 마지막 열까지, 이전 열의 정보를 통해서 동적 프로그래밍 실행
# 점화식 : dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + maze[i][j] (단, 0 < i)
# i가 0일 때를 가정하여 추가적인 점화식을 설계해야 함. (dp[i][j] = dp[i][j-1] + maze[i][j])
if M > 1:
    for j in range(1, M):
        for i in range(N):
            if i == 0:
                dp[0][j] = dp[0][j-1] + maze[0][j]
            else:
                # 현재 좌표 (i,j) 를 기준으로 좌측, 좌측 상단, 상단 총 3가지의 경우를 고려
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + maze[i][j]
print(dp[N-1][M-1])
