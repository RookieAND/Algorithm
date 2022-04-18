import sys
num = int(sys.stdin.readline())
data = [i for i in range(1, num + 1)]
data.reverse()
list(map(lambda x: print(x), data))