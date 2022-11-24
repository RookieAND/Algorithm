import sys

read = sys.stdin.readline
N, A, X = int(read()), sorted(list(map(int, read().split()))), int(read())
start, end, result = 0, len(A) - 1, 0

while start < end:
    summary = A[start] + A[end]
    if summary == X:
        result += 1
    # 합계가 X보다 작다면, 시작 인덱스를 1칸 좁힌다.
    elif summary < X:
        start += 1
        continue
    # 합계가 X보다 크거나 같다면, 끝 인덱스를 1칸 좁힌다.
    end -= 1
print(result)
