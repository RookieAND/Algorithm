import sys

read = sys.stdin.readline
N, houses = int(read()), sorted(list(map(int, read().split())))
print(houses[(N - 1) // 2])

