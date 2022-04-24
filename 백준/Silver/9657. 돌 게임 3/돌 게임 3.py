import sys

n = int(sys.stdin.readline())

# dp[i] 는 돌이 i개 놓인 경우, 누가 승리하였는지에 대한 안내를 저장
# 만약 현재 돌에서 1, 3, 4개를 뺀 갯수로 게임을 진행하였을 때 상대가 이겼다면,
# 이번 턴에서는 내가 무조건 승리할 수 있다는 의미.
dp = [None, 'SK', 'CY', 'SK', 'SK'] + [0] * (n-4)


for i in range(5, n+1):
    if dp[i-1] == 'SK' and dp[i-3] == 'SK' and dp[i-4] == 'SK':
        dp[i] = 'CY'
    else:
        dp[i] = 'SK'
print(dp[n])
