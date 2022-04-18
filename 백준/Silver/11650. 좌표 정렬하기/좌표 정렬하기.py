import sys

n = int(sys.stdin.readline())
data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
data.sort(key=lambda x: x[1])
list(map(lambda x: print(f"{x[0]} {x[1]}"), sorted(data)))
