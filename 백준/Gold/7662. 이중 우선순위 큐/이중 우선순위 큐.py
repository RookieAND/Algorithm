import sys
import heapq

read = sys.stdin.readline
T = int(read())

for _ in range(T):
    Q = int(read())
    heap_min, heap_max = [], []
    is_exist = [False] * Q

    for idx in range(Q):
        operator, value = read().split()

        if operator == 'I':
            heapq.heappush(heap_min, (int(value), idx))
            heapq.heappush(heap_max, (-int(value), idx))
            is_exist[idx] = True
            continue

        # D -1 일 경우, 최솟값을 삭제해야 함.
        if value == '-1':
            # 삭제 전, 최대 힙에서 이미 삭제된 값이 있다면 이를 먼저 반영해야 함.
            while heap_min and not is_exist[heap_min[0][1]]:
                heapq.heappop(heap_min)
            # 전처리 과정 후, 최소 힙에 값이 있다면 이를 추가적으로 제거.
            if heap_min:
                # 현재 삭제하려는 값을 먼저 제거 처리 하고, 실 제거 진행.
                is_exist[heap_min[0][1]] = False
                heapq.heappop(heap_min)

        # D 1 일 경우, 최댓값을 삭제해야 함.
        else:
            # 삭제 전, 최소 힙에서 이미 삭제된 값이 있다면 이를 먼저 반영해야 함.
            while heap_max and not is_exist[heap_max[0][1]]:
                heapq.heappop(heap_max)
            if heap_max:
                is_exist[heap_max[0][1]] = False
                heapq.heappop(heap_max)


    # 연산을 마친 후, 두 힙을 동기화하는 작업을 추가적으로 거침.
    while heap_min and not is_exist[heap_min[0][1]]:
        heapq.heappop(heap_min)
    while heap_max and not is_exist[heap_max[0][1]]:
        heapq.heappop(heap_max)

    if not heap_max and not heap_min:
        print("EMPTY")
    else:
        print(f"{-heap_max[0][0]} {heap_min[0][0]}")