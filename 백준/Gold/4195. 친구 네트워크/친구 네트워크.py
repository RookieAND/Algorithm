# parent = {Fred: Fred, Barney: Fred, Betty: Fred, Wilma: Fred}

import sys

read = sys.stdin.readline

def find(x):
    if friend[x] != x:
        friend[x] = find(friend[x])
    return friend[x]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    # b 집합을 a 집합에 포함시킨다.
    friend[b] = a
    # b 집합이 a 집합에 포함될 경우, b 집합에 소속되어 있던 원소의 수량도 더해야 한다.
    participants[a] += participants[b]


for _ in range(int(read())):
    friend = dict() # 참여자가 소속된 트리의 루트 노드를 담는 딕셔너리
    participants = dict() # 참여자를 루트 노드라고 가정했을 때, 하위에 놓인 노드의 수량
    for _ in range(int(read())):
        a, b = read().split()
        if a not in friend:
            friend[a] = a
            participants[a] = 1
        if b not in friend:
            friend[b] = b
            participants[b] = 1
        union(a, b)
        # a 집합이 b 집합을 포함 시키므로, 무조건 a 집합에 할당된 노드의 수를 구해야 함.
        print(participants[find(a)])
        