import sys

N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

# 전체 예산 중 0과 가장 큰 값 예산 값을 선별하여 탐색 범위를 지정
start, end = 0, max(budgets)
# 이분 탐색을 시작함. 중간 값을 상한선으로 두어 나온 예산의 총합이 M보다 같거나 작은지를 판단.
# 만약 조건을 만족하였을 경우, 도출된 상한선을 구하고 이것이 이전의 결과보다 큰 값인지를 판별
while start <= end:
    mid = (start + end) // 2
    total = 0
    for budget in budgets:
        total += mid if budget >= mid else budget
    if total > M:
        end = mid - 1
    elif total <= M:
        start = mid + 1

# 상한선보다 최대 예산이 더 크다면 상한선을, 그렇지 않다면 최대 예산을 출력
print(end)