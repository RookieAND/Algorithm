from math import ceil
a, b, c = tuple(map(int, input().split()))
print(int(a / (c - b)) + 1 if c - b != 0 and ceil(a / (c - b)) + 1 > 0 else -1)