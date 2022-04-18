import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start, end, result = 1, k, 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, N+1):
        count += min(mid // i, N)
    if count >= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)
