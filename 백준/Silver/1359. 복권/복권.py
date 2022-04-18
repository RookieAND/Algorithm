import sys
import itertools as itr

n, m, k = map(int, sys.stdin.readline().split())
total, win = 0, 0

def check_match(c1, c2):
    count = 0
    for num in c1:
        if num in c2:
            count += 1
    return count

for c1 in itr.combinations(range(1, n+1), m):
    for c2 in itr.combinations(range(1, n+1), m):
        total += 1
        c1, c2 = sorted(c1), sorted(c2)
        if check_match(c1, c2) >= k:
            win += 1

print(win/total)