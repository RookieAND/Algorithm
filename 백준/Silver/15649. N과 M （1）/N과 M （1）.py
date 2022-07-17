import sys

N, M = list(map(int, input().split()))
S = []

def dfs():
    if len(S) == M:
        print(' '.join(map(str, S)))
        return

    for i in range(1, N + 1):
        if i not in S:
            S.append(i)
            dfs()
            S.pop()


dfs()