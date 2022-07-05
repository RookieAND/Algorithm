import sys
import heapq

read = sys.stdin.readline
N, centi_height, T = map(int, read().split())

heap = [-int(read()) for _ in range(N)]
heapq.heapify(heap)

count = 0
for _ in range(T):
    if -heap[0] < centi_height or -heap[0] == 1:
        break
    heapq.heapreplace(heap, -(-heap[0] // 2))
    count += 1

if -heap[0] < centi_height:
    print('YES', count, sep='\n')
else:
    print('NO', -heap[0], sep='\n')