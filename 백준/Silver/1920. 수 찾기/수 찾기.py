import sys

n = int(sys.stdin.readline())
a = set(sys.stdin.readline().split())
m = int(sys.stdin.readline())
b = sys.stdin.readline().split()

for num in b:
    print(1 if num in a else 0)