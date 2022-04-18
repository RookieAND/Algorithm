import sys
import itertools as itr

n, s = map(int, sys.stdin.readline().split())
data, result = list(map(int, sys.stdin.readline().split())), 0

for i in range(1, n+1):
    for c in itr.combinations(data, i):
        if sum(c) == s:
            result += 1
print(result)
