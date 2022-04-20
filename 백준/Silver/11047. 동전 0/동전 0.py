import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
# 가치가 작은 순부터 입력되었으므로, 이를 역순으로 돌려 큰 수부터 오도록 한다.
coins.sort(reverse=True)

# 큰 가치의 동전이 작은 가치의 동전의 배수라면, 그리디 알고리즘으로 풀이가 가능.
# 큰 가치를 지닌 동전부터 작은 가치를 지닌 동전 순으로 나누어 개수의 합을 구함.
left_money, result = k, 0
for coin in coins:
    result += left_money // coin
    left_money = left_money % coin
    if left_money == 0:
        break
print(result)