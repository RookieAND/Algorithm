import sys

n, current = int(sys.stdin.readline()), 0
data = sorted(list(set(sys.stdin.readline().strip() for _ in range(n))))
data.sort(key=lambda x: len(x))
list(map(lambda x: print(x), data))
