import sys

coins = [500, 100, 50, 10, 5, 1]
n, result = int(sys.stdin.readline()), 0
left_money = 1000 - n

# 동전은 가치가 큰 순서부터 낮은 순서대로 진행
for coin in coins:
    # 아직 잔돈이 남아있다면, 해당 동전을 최대로 사용하여 잔돈에서 제외
    if left_money > 0:
        coin_amount = left_money // coin
        result += coin_amount
        left_money -= coin * coin_amount
    else:
        break
print(result)