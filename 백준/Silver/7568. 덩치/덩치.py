import sys

n = int(sys.stdin.readline())
data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = []
for i in range(n):
    rank = 1
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank += 1
    result.append(rank)
list(map(lambda x: print(x, end=" "), result))