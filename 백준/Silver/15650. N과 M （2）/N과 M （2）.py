import sys

N, M = list(map(int, input().split()))
S = []

def dfs(start):
    if len(S) == M:
        print(' '.join(map(str, S)))
        return

    for i in range(start, N + 1):
        if i not in S:
            S.append(i)
            dfs(i + 1)
            S.pop()


dfs(1)