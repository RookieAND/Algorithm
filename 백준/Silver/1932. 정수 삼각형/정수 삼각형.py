import sys

n = int(sys.stdin.readline())
triangle, dp = [], [[0] * n for _ in range(n)]
# dp[i][j] 는 i열 j행에서 가능한 최댓값을 저장하고자 하는 메모이제이션
# i열에는 최대 i행까지의 배열이 할당되며 (j <= i) 이는 모든 i열에 해당됨
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

if n == 1:
    print(triangle[0][0])
else:
    # 1열 1행 (가장 꼭대기에 위치한 곳) 의 값을 dp에 초기화 시킴.
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i+1):
            # 만약 행이 0이라면 (삼각형의 왼쪽 변이라면) 점화식 : dp[i][j] = dp[i-1][j]
            if j == 0:
                dp[i][j] = dp[i-1][j]
            # 만약 해당 열이 해당 행의 최하단이라면, 점화식 : dp[i][j] = dp[i-1][j-1]
            elif j == i:
                dp[i][j] = dp[i-1][j-1]
            # 그렇지 않을 경우 점화식 : dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
            # 현재 삼각형 위치에 설정된 값을 마저 추가해야 함.
            dp[i][j] += triangle[i][j]

    # 삼각형의 가장 마지막 줄에서 제일 큰 값을 산출하여 출력시킴
    print(max(dp[n-1]))