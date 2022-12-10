import sys
sys.setrecursionlimit(10 ** 6)


def dfs(i):
    global result
    visited[i] = True
    cycle.append(i)
    next = student[i]

    # 현재 좌표를 방문하였는지 체크헤야 함.
    if visited[next]:
        # 만약 next 를 방문하였고 cycle 내에 있다면, next 부터 사이클이 시작된 것.
        if next in cycle:
            result += cycle[cycle.index(next):]
        return
    # 미방문한 경우, 다음 좌표를 탐색함.
    else:
        dfs(next)

read = sys.stdin.readline
T = int(read())
for _ in range(T):
    N = int(read())
    student = [0] + list(map(int, read().split()))
    visited = [False] * (N + 1)
    result = []
    for i in range(1, N + 1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(N - len(result))