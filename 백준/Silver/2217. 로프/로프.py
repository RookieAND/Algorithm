import sys

read = sys.stdin.readline
N = int(read())
roofs = sorted([int(read()) for _ in range(N)], reverse=True)

result = 0
for idx in range(len(roofs)):
    maximun_weight = roofs[idx] * (idx + 1)
    result = max(result, maximun_weight)

print(result)