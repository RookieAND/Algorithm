import sys

read = sys.stdin.readline
N = int(read())
number = list(map(int, read().split()))
print(min(number), max(number))