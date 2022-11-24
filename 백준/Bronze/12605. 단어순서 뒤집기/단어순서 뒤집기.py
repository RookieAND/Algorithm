import sys

read = sys.stdin.readline
N = int(read())
for num in range(1, N + 1):
    words = read().rstrip().split()
    print(f"Case #{num}: " + " ".join(words[::-1]))