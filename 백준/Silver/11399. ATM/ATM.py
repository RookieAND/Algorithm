import sys

n = int(sys.stdin.readline())
pi = list(map(int, sys.stdin.readline().split()))
sumpi = [0] * n
# 시간이 빨리 걸리는 사람들부터 먼저 ATM기를 사용하게 해야 함.
# 시간이 적은 사람이 먼저 작업을 수행하면 그만큼 누적합이 작아지기 때문.
pi.sort()
sumpi[0] = pi[0]

# 2번째 사람부터 N번째 사람까지 걸리는 모든 시간을 계산
for i in range(1, n):
    sumpi[i] = sumpi[i-1] + pi[i]

print(sum(sumpi))


