# 만약 둘이 적대 관계여야 하는데 동맹 관계라면 이론이 틀린 것임
# 만약 둘이 적대 관계라면, a의 적 관계를 b의 동맹 관계로 설정해야 함. 반대도 마찬가지.

import sys

read = sys.stdin.readline
N, M = map(int, read().split())

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    parents[ra] = rb


# 자신이 속한 그룹의 루트 노드를 담는 parents, 자신이 적대한 그룹의 루트 노드를 담는 enemys
parents = [i for i in range(N + 1)]
enemys = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, read().split())
    ra, rb = find(a), find(b)
    # 두 그룹은 서로 적대 관계여야 하는데, 같은 그룹에 놓일 경우 말이 안됨.
    if ra == rb:
        print(0)
        sys.exit(0)
    # a와 적대관계에 놓인 그룹이 아직 없는 경우, b가 속한 그룹을 지정함.
    # a와 적대관계에 놓인 그룹이 있는 경우, a의 적대 관계에 놓인 그룹에 b를 포함시킴.
    if enemys[a] == 0:
        enemys[a] = rb
    else:
        union(enemys[a], rb)

    # b 또한 위에서 했던 작업을 그대로 진행하면 됨.
    if enemys[b] == 0:
        enemys[b] = ra
    else:
        union(enemys[b], ra)
print(1)