import sys
import collections

n = int(sys.stdin.readline().strip())
data = collections.deque((range(1, n+1)))

while len(data) > 1:
    data.popleft()
    data.rotate(-1)
print(data[0])