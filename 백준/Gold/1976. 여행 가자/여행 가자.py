import sys

read = sys.stdin.readline

N = int(read())
M = int(read())

# 각 노드들의 루트 노드에 대한 정보를 담은 list parent
parent = list(range(N + 1))

def find(x):
    # 현재 루트 노드가 아닐 경우, 경로 압축과 함께 재귀 진행.
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a, root_b = find(a), find(b)
    # a, b의 루트 노드가 동일하다면, Union을 진행할 이유가 없음.
    if root_a == root_b:
        return
    parent[max(root_a, root_b)] = min(root_a, root_b)

for current_city in range(1, N + 1):
    # i번째 도시와 나머지 도시에 대한 연결 정보를 담은 connection_info
    connection = list(map(int, read().split()))
    for other_city in range(1, N + 1):
        # 자기 자신에 대한 정보는 굳이 판별하지 않아도 됨.
        if current_city == other_city:
            continue
        # 만약 다른 도시와의 연결 정보가 1이라면, 연결이 되었다는 의미.
        # 따라서 두 노드를 Union 으로 묶어 동일한 집합에 위치시켜야 함.
        elif connection[other_city - 1]:
            union(current_city, other_city)

travel_plan = list(map(int, read().split()))
for idx in range(M - 1):
    f_city, s_city = travel_plan[idx], travel_plan[idx + 1]
    # 다음으로 이동해야 하는 도시와 현재 도시가 동일한 집합 (루트 노드) 인지 확인.
    # parent 노드는 0부터 시작하므로 각각 1씩 제거해줘야 함.
    if find(f_city) != find(s_city):
        print('NO')
        sys.exit(0)

# 예외 사항에 걸리지 않았다면 YES 출력
print('YES')
