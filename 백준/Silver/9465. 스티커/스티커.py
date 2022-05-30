import sys

read = sys.stdin.readline
T = int(read())

for _ in range(T):
    N = int(read())
    # dp[i][j] 는 i열 j행의 스티커를 선택할 경우, 얻는 점수의 최댓값을 저장
    # 우선 각 열과 행에 놓인 스티커의 점수로 메모이제이션을 초기화 해야 함.
    dp = [list(map(int, read().split())) for _ in range(2)]
    # 1행에 위치한 스티커 점수 값은, 대각선에 위치한 이전 행의 점수를 더해주면 됨.
    # 단, 이는 N이 2 이상일 때만 가능하므로 조건식으로 체크를 해주어야 함
    if N > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

    # N이 3 이상일 때는 아래와 같은 점화식 진행이 가능하다.
    if N > 2:
        # 점화식 : 행이 2 이상이라면 바로 이전 행을 택할 지, 2칸 전의 행을 택할지 정할 수 있다.
        # dp[i][j] += max(dp[not i][j - 1], dp[not i][j - 2]))
        for i in range(2, N):
            dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
            dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])

    print(max(dp[0][N-1], dp[1][N-1]))