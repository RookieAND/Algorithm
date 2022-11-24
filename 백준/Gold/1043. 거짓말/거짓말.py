import sys

read = sys.stdin.readline
N, M = map(int, read().split())
know_true = set(read().split()[1:])

# 파티 그룹을 우선 집계하여 이를 체크.
parties = [set(read().split()[1:]) for _ in range(M)]

# 파티를 진행하면서, 진실을 알게 된 이들을 체크.
for _ in range(M): 
    for party in parties:
        # 파티 인원 중, 진실을 아는 이들이 있다면 모든 참가자를 포함시킴.
        if know_true.intersection(party):
            know_true = know_true.union(party)

# 파티 구성원 중, 진실을 알게 된 이들이 포함되지 않은 파티만 체크.
result = 0
for party in parties:
    if not know_true.intersection(party):
        result += 1
print(result)