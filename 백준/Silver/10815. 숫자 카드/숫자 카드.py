import sys

read = sys.stdin.readline
N = int(read())
card = list(map(int, read().split()))
# 카드를 정렬하고, 최솟값과 최댓값을 찾아 탐색 범위의 시작과 끝을 정한다.
card.sort()
# M개의 카드를 입력 받고, 각각의 수에 대한 이분 탐색을 시행한다.
M = int(read())
number = list(map(int, read().split()))

for num in number:
    # 이분 탐색 범위는 상근이가 보유한 카드 전체다.
    start, end = 0, len(card) - 1
    is_exist = False
    while start <= end:
        mid = (start + end) // 2
        mid_card = card[mid]
        # 만약 일치하는 값이 나왔다면 카드를 가진 것이라고 판단.
        if num == mid_card:
            is_exist = True
            break
        if num < mid_card:
            end = mid - 1
            continue
        if num > mid_card:
            start = mid + 1
    print(1 if is_exist else 0, end=' ')
