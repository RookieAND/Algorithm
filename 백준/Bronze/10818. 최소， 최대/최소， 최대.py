import sys
count = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
print(arr[0], arr[len(arr) - 1])