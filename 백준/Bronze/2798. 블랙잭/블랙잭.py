import sys
import itertools as itr

n, m = map(int, sys.stdin.readline().split())
data, best_sum = list(map(int, sys.stdin.readline().split())), 0
for c in itr.combinations(data, 3):
    if sum(c) == m:
        best_sum = m
        break
    elif best_sum < sum(c) < m:
        best_sum = sum(c)
print(best_sum)