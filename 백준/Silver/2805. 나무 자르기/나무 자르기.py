import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
min_h, max_h = 1, max(trees)

while min_h <= max_h:
    mid_h, total = (min_h + max_h) // 2, 0
    for tree in trees:
        total += tree - mid_h if tree > mid_h else 0
    if total > M:
        min_h = mid_h + 1
    elif total < M:
        max_h = mid_h - 1
    else:
        max_h = mid_h
        break
print(max_h)