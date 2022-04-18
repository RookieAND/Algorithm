import sys
n, x = tuple(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
list(map(lambda x: print(str(x) + " ", end=""), [i for i in a if i < x]))