import sys

read = sys.stdin.readline
N, M = map(int, read().split())

S = [read().rstrip() for _ in range(N)]

check = {}
for _ in range(M):
    sentence = read().rstrip()
    if sentence not in check:
        check[sentence] = 1
    else:
        check[sentence] += 1

print(sum([check[word] for word in S if word in check]))