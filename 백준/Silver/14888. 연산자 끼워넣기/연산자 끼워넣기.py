import sys
from math import inf

read = sys.stdin.readline
N = int(read())
numbers = list(map(int, read().split()))
oper_num = list(map(int, read().split()))

MAX, MIN = -inf, inf

def dfs(dep, result, add, sub, mul, div):
    global MAX, MIN
    if dep == N:
        MAX = max(result, MAX)
        MIN = min(result, MIN)
        return

    if add:
        dfs(dep + 1, result + numbers[dep], add - 1, sub, mul, div)
    if sub:
        dfs(dep + 1, result - numbers[dep], add, sub - 1, mul, div)
    if mul:
        dfs(dep + 1, result * numbers[dep], add, sub, mul - 1, div)
    if div:
        dfs(dep + 1, int(result / numbers[dep]), add, sub, mul, div -1)

dfs(1, numbers[0], oper_num[0], oper_num[1], oper_num[2], oper_num[3])
print(MAX)
print(MIN)