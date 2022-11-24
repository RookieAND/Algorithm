import sys

read = sys.stdin.readline
score = [100, 100]

N = int(read())

for _ in range(N):
    first, second = map(int, read().split())
    if first < second:
        score[0] -= second
    elif first > second:
        score[1] -= first

print(*score, sep='\n')