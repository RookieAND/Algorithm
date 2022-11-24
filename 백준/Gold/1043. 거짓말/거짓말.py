import sys

# x 노드가 속한 집합의 루트 노드를 탐색하는 함수.
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])

    return parents[x]

def union(a, b):
    a, b = find(a), find(b)

    # 둘 다 진실을 아는 경우, 굳이 Union을 안해도 됨.
    if a in know_true and b in know_true:
        return

    # a 가 진실을 아는 집합에 소속되어 있다면, b가 소속된 집합을 포함시킴.
    if a in know_true:
        parents[b] = a

    # b 가 진실을 아는 집합에 소속되어 있다면, a가 소속된 집합을 포함시킴.
    elif b in know_true:
        parents[a] = b

    # 루트 노드가 같지 않을 경우, 두 집합을 서로 이어줌.
    # 여기서는 노드의 값이 큰 것이 작은 것에 연결되게끔 함.
    else:
        parents[max(a, b)] = min(a, b)

read = sys.stdin.readline
N, M = map(int, read().split())
know_true = list(map(int, read().split()))[1:]

# 유니온 파인드 연산을 위해, 각 노드 별 루트 노드를 보관하는 list.
parents = list(range(N + 1))
parties = []

for _ in range(M):
    peoples, *party = list(map(int, read().split()))
    # 해당 파티의 참가자들을 대상으로 Union - Find 진행.
    for i in range(peoples - 1):
        union(party[i], party[i + 1])
    parties.append(party)

result = 0
for party in parties:
    for visitor in party:
        # 만약 해당 파티의 참가원이 속한 그룹의 루트 노드가 진실을 아는 이라면, 해당 파티 제외.
        if find(visitor) in know_true:
            break
    else:
        result += 1

print(result)