import sys
sys.setrecursionlimit(10 ** 5)

# 이진 탐색을 통해 후위 탐색 결과를 출력시키는 함수.
def post_order(start, end):
    if start > end:
        return
    # 전위 탐색은 루트 노드가 맨 앞에 위치하므로, 이를 root로 설정.
    root = pre_order[start]
    index = start + 1
    # 루트 노드 바로 다음 인덱스부터 끝까지 이진 탐색 시작.
    # root 값보다 더 큰 값이 나오기 전까지 index 범위 증가.
    while index <= end:
        if pre_order[index] > root:
            break
        index += 1
    # 시작 범위부터 root 값보다 작은 범위까지 후위 탐색
    post_order(start + 1, index - 1)
    # root 값보다 큰 범위에서 끝 범위까지 후위 탐색.
    post_order(index, end)
    # 탐색을 모두 마쳤다면, 루트 노드 출력
    print(root)

# try-except 로 입력이 종료될때까지 전위 탐색 결과를 받음.
pre_order = []
while True:
    try:
        pre_order.append(int(sys.stdin.readline()))
    except:
        break

post_order(0, len(pre_order) - 1)