import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
dp = [{} for _ in range(N)]
dp[1] = {numList[0]: 1}

for i in range(2, N):
    for num, amount in dp[i-1].items():
        if 0 <= num + numList[i-1] <= 20:
            if num + numList[i-1] not in dp[i]:
                dp[i][num + numList[i - 1]] = amount
            else:
                dp[i][num + numList[i-1]] += amount
        if 0 <= num - numList[i-1] <= 20:
            if num - numList[i-1] not in dp[i]:
                dp[i][num - numList[i - 1]] = amount
            else:
                dp[i][num - numList[i-1]] += amount

result = numList[-1]
print(dp[N-1][result])