import sys

N, C = map(int, sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for _ in range(N)])
min_x, max_x, result = 1, house[-1] - house[0], 0

def count_wifi(d):
    count = 1
    start_point = house[0]
    for i in range(len(house)):
        if house[i] - start_point >= d:
            start_point = house[i]
            count += 1
    return count

while min_x <= max_x:
    mid_x = (min_x + max_x) // 2
    amount = count_wifi(mid_x)
    if amount >= C:
        result = mid_x
        min_x = mid_x + 1
    else:
        max_x = mid_x - 1

print(result)