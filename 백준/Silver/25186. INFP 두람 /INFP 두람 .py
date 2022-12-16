import sys

read = sys.stdin.readline
N = int(read())
D = list(map(int, read().split()))

if N == 1 and D[0] == 1:
    print("Happy")
    sys.exit(0)

max_count = max(D)
total_count = sum(D)
print("Unhappy" if total_count < max_count * 2 else "Happy")