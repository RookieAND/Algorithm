import sys
from math import inf

n, m, b = map(int, sys.stdin.readline().split())
region, result = [], []
for i in range(n):
    region.append(list(map(int, sys.stdin.readline().split())))

min_h, max_h = min(map(lambda x: min(x), region)), max(map(lambda x: max(x), region))
least_time, best_height = inf, 256

def check_time(h):
    need_block, has_block = 0, 0
    for j in range(n):
        for k in range(m):
            current_h = region[j][k]
            if current_h == h:
                continue
            elif current_h > h:
                has_block += current_h - h
            elif current_h < h:
                need_block += h - current_h
    if need_block <= has_block + b:
        return has_block * 2 + need_block
    else:
        return None

for h in range(min_h, max_h+1):
    time = check_time(h)
    if time is not None:
        if time <= least_time:
            least_time, best_height = time, h
print(least_time, best_height)

