import sys
from collections import deque

num, result = int(sys.stdin.readline()), []
for _ in range(num):
    n, m = map(int, sys.stdin.readline().split())
    que = deque(map(int, sys.stdin.readline().split()))
    cnt = 0
    while que:
        first = max(que)
        removed = que.popleft()
        m -= 1
        if removed != first:
            que.append(removed)
            if m < 0:
                m = len(que)-1
        else:
            cnt += 1
            if m == -1:
                result.append(cnt)
                break

list(map(lambda x: print(x), result))