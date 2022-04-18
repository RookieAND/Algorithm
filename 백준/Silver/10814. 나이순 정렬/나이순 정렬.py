import sys

n = int(sys.stdin.readline())
data = list(tuple(sys.stdin.readline().split()) for _ in range(n))
data.sort(key=lambda x: int(x[0]))
list(map(lambda x: print(x[0]+" "+x[1]), data))