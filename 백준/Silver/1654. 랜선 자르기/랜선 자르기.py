import sys

k, n = map(int, sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(k)]
min_len, max_len = 1, max(data)

while min_len <= max_len:
    mid_len = (min_len + max_len) // 2
    count = 0
    for line in data:
        count += line // mid_len
    if count >= n:
        min_len = mid_len + 1
    else:
        max_len = mid_len - 1
        
print(max_len)