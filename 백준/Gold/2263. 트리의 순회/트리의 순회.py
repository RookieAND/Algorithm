import sys
sys.setrecursionlimit(10 ** 5)

read = sys.stdin.readline
N = int(read())
in_order = list(map(int, read().split()))
post_order = list(map(int, read().split()))

# 중위 탐색 결과들이 몇 번째 인덱스에 있는지를 저장하는 List
position = [0] * (N + 1)
for i in range(N):
    position[in_order[i]] = i


def pre_order(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    root = post_order[post_end]
    print(root, end=' ')
    # 좌측 서브 트리와 우측 서브 트리의 노드 수량을 계산
    left = position[root] - in_start
    right = in_end - position[root]

    # 좌측 서브 노드와 우측 서브 노드에 해당되는 영역을 주고, 재귀 함수 실행
    pre_order(in_start, in_start + left - 1, post_start, post_start + left - 1)
    pre_order(in_end - right + 1, in_end, post_end - right, post_end-1)


pre_order(0, N-1, 0, N-1)