# 친구를 사귈 때마다 각 친구가 요구하는 친구 비를 지급해야 한다.
# 여러 친구를 사귀면 각 친구들이 요구하는 친구 비를 전부 납입해야 한다.
# 따라서 각 그룹 별로 내야 하는 친구비의 총합을 업데이트 하면서, 가장 싼 비용을 찾는다.
# 이후 해당 작업을 반복하고, 각 그룹 별로 필요한 최소 금액을 합하여 K보다 낮은지 본다.

import sys

read = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    # 두 그룹 중, 가장 낮은 친구비를 가진 그룹을 소속의 주체로 설정.
    if cost[a] > cost[b]:
        parents[a] = b
    else:
        parents[b] = a


N, M, K = map(int, read().split())
cost = [0] + list(map(int, read().split()))
parents = [i for i in range(N + 1)]

for _ in range(M):
    v, w = map(int, read().split())
    union(v, w)


# 집합 관계가 형성되었다면, 각 집합 별로 내야 할 친구비를 합산해야 함.
total_spend = 0
for idx, root in enumerate(parents):
    if root == idx:
        total_spend += cost[root]

print(total_spend if total_spend <= K else "Oh no")
