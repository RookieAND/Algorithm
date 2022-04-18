import sys

data = list(int(sys.stdin.readline().strip()) for _ in range(int(sys.stdin.readline())))
data.sort()
list(map(lambda x: print(x), data))