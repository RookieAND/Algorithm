import sys

n = int(sys.stdin.readline())
# consult는 (시간, 수익) 이 튜플로 담긴 list 이다. index + 1은 해당 상담이 진행되는 일수다.
consult = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    time, cost = consult[i]
    # 퇴사일 전까지 진행할 수 없는 상담이라면, 그 다음날에 현재까지 모인 수익금을 그대로 이전시킴
    if time + i > n:
        dp[i] = dp[i+1]
    # 당일에 상담을 진행하는 것이 더 이득이 큰지, 상담을 넘기는 것이 이득인지를 판별
    # i일에 걸린 상담을 진행하는 경우는, dp[i+time] + cost 이고, 이를 넘기는 경우는 dp[i+1] 이다.
    # 핵심 점화식 : dp[i] = max(dp[i+1], cost + dp[i+time])
    else:
        dp[i] = max(cost + dp[i + time], dp[i + 1])
# i 가 0일 경우 최댓값이 저장되므로 이를 출력
print(dp[0])