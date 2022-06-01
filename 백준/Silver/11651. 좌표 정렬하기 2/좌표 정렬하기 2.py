import sys

n = int(sys.stdin.readline())
data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
data.sort(key=lambda x: x[0])
data.sort(key=lambda x: x[1])
for dt in data:
    print(f"{dt[0]} {dt[1]}")