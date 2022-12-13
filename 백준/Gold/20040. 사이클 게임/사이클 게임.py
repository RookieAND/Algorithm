import sys
sys.setrecursionlimit(10 ** 6)

read = sys.stdin.readline

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    parents[b] = a


N, M = map(int, read().split())
parents = [i for i in range(N + 1)]
for idx in range(1, M + 1):
    a, b = map(int, read().split())
    # 점을 이은 후 두 점의 루트 노드가 동일하다면, 사이클이 생성된 것임.
    if find(a) == find(b):
        print(idx)
        sys.exit()
    union(a, b)

# 사이클이 만들어지지 않은 경우 0 출력.
print(0)