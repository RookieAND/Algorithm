import sys
from math import inf

X, Y = map(int, sys.stdin.readline().split())
current_win = Y * 100 // X

start, end = 1, X

result = inf
while start <= end:
    mid = (start + end) // 2
    next_win = (Y + mid) * 100 // (X + mid)
    # 승률이 올라갔다면, 그만큼 많이 이겼으므로 끝 범위 축소.
    if next_win > current_win:
        result = min(mid, result)
        end = mid - 1
    # 승률이 그대로일 경우, 더 많이 이겨야 하므로 시작 범위 증가.
    else:
        start = mid + 1

print(result if result != inf else -1)