import sys

n, result = int(sys.stdin.readline()), None
for i in range(n):
    if sum(map(int, str(i))) + i == n:
        result = i
        break
if result is None:
    print(0)
else:
    print(result)