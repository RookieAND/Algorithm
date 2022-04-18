import sys

_ = int(sys.stdin.readline())
card = sorted(list(map(int, sys.stdin.readline().split())))
_ = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))

result = {}
for num in card:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1

print(' '.join(str(result[num]) if num in result else '0' for num in numList))