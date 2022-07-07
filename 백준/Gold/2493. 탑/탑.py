import sys

read = sys.stdin.readline

N = int(read())
towers = list(map(int, read().split()))
result = [0 for _ in range(N)]

# 의미있는 탑의 정보를 (인덱스, 높이) 로 저장함.
stack = []
for i in range(N):
    # 의미있는 탑을 높이가 낮은 순대로 하나씩 꺼내어 대조함.
    while stack:
        # 만약 가장 높이가 낮은 탑보다 현재 탑의 높이가 낮다면?
        # 해당 탑은 가장 높이가 낮은 의미있는 탑과의 교신이 가능.
        if towers[i] < stack[-1][1]:
            result[i] = stack[-1][0] + 1
            break
        # 그렇지 않을 경우 해당 탑을 제거하고, 그 다음으로 높이가 낮은 탑을 꺼내옴.
        stack.pop()
    # 스택이 비거나 더 이상의 비교가 불가할 경우, 현재 탑의 정보를 추가해야 함.
    stack.append((i, towers[i]))

print(*result)