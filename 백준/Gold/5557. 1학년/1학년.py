import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
# dp[i][j] 에서, i는 사용한 숫자의 수량이며 j에는 i개의 숫자를 사용할 경우 나오는 결과값을 저장한 dict를 담는다.
# dp[i] 에는 dp[i-1] 까지의 결과 값들에 numList[i-1] 을 더하거나 뺀 값이 0 초과 20 미만일 경우 이를 추가한다.
# dp[i] = {sum: amount} 형식으로 저장됨. key는 수식의 결과이며 amount 는 해당 결과가 나오는 수식의 개수이다.
dp = [{} for _ in range(N)]
dp[1] = {numList[0]: 1}

# i 번째 수를 사용하였을 때 나올 수 있는 모든 합계를 구하기 위해 반복을 돌림
for i in range(2, N):
    # i-1 번째 수를 사용하였을 때 나온 모든 경우의 수를 순차적으로 반복시킴
    for num, amount in dp[i-1].items():
        # i-1 번째 수를 사용하여 나온 합계 + i 번째 수가 0 이상 20 이하인지를 판별
        if 0 <= num + numList[i-1] <= 20:
            if num + numList[i-1] not in dp[i]:
                dp[i][num + numList[i - 1]] = amount
            else:
                dp[i][num + numList[i-1]] += amount
        # i-1 번째 수를 사용하여 나온 합계 - i 번째 수가 0 이상 20 이하인지를 판별
        if 0 <= num - numList[i-1] <= 20:
            if num - numList[i-1] not in dp[i]:
                dp[i][num - numList[i - 1]] = amount
            else:
                dp[i][num - numList[i-1]] += amount

result = numList[-1]
print(dp[N-1][result])
