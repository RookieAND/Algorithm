import sys

read = sys.stdin.readline
N, K = map(int, read().split())
numbers = list(map(int, read().split()))

result = [sum(numbers[:K])]
for i in range(N - K):
    result.append(result[i] - numbers[i] + numbers[K + i])

print(max(result))