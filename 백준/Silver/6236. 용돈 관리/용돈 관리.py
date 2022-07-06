import sys

read = sys.stdin.readline

N, M = map(int, read().split())
costs = [int(read()) for _ in range(N)]

# 인출 금액이 최대 지출 비용보다는 커야 하므로, 시작 지점을 지출 비용의 최댓값으로 설정.
# 지출 비용의 총합보다는 인출 금액이 작아야 하므로, 끝 지점은 지출 비용의 총합으로 설정.
start, end, result = max(costs), sum(costs), sum(costs)

def check(K):
    count, current = 1, K
    for cost in costs:
        # 현재 보유 금액이 지출 비용보다 더 적을 경우,
        # K원을 새롭게 꺼내어 지갑에 충전시켜야 함.
        if current - cost < 0:
            current = K
            count += 1
        current -= cost
    # 반복이 완료되었다면, 총 인출 횟수를 리턴함.
    return count


while start <= end:
    mid = (start + end) // 2
    check_count = check(mid)
    # 만약 인출 횟수가 많거나 -1이 나왔다면, 금액 상향
    if check_count > M:
        start = mid + 1
        continue
    # 그렇지 않다면 금액 범위를 낮추고, 정답을 추출함.
    end = mid - 1
    result = mid

print(result)
