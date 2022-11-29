import sys

read = sys.stdin.readline
N, M = map(int, read().split())

matrix = [list(map(int, read().split())) for _ in range(N)]
# 메모이제이션 배열은 0행과 0열에 대한 값도 추가해서 확장한다.
# 이럴 경우 1행, 1열에 대한 예외 처리를 하지 않아도 되서 좋다.
dp = [[0] * (N + 1) for _ in range(N + 1)]

# 메모이제이션 작업
for row in range(1, N + 1):
    for col in range(1, N + 1):
        dp[row][col] = dp[row - 1][col] + dp[row][col - 1] - dp[row - 1][col - 1] + matrix[row - 1][col - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, read().split())
    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)
