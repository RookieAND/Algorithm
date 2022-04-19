import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]

# dp[i] 는 i원을 만드는 모든 경우의 수를 저장, dp[0] 은 0원이므로 그대로 메모이제이션 초기화.
dp = [1] + [0 for _ in range(k)]

# 각각의 동전을 대조하여, 해당 동전을 추가한 금액의 경우의 수가 현재보다 더 큰지를 판별
# 동전이 하나씩 추가되면서 생기는 경우의 수를 각 금액 별로 파악하여 메모이제이션에 추가하는 방식
for coin in coins:
    # 1원부터 m원까지 각 금액에 따른 경우의 수를 순차적으로 탐색.
    for cost in range(1, k + 1):
        # 현재 금액이 동전의 가치보다 우선 높아야 함 (낮을 경우 사용 불가)
        # 만약 i원에서 동전의 가치를 뺀 금액의 경우의 수가 존재한다면, 이를 추가함.
        # 현재 금액에 대한 경우의 수는 현재 금액에서 동전의 가치를 제했을 때 나오는 경우의 수들의 합산과 같다.
        if cost >= coin:
            dp[cost] += dp[cost - coin]

# k원일 때 존재하는 경우의 수를 최종적으로 출력시킴
print(dp[k])