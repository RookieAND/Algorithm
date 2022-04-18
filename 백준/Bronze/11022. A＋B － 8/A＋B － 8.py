import sys

count, data = int(sys.stdin.readline()), []
for _ in range(0, count):
    data.append(tuple(map(int, sys.stdin.readline().split())))
for i in range(0, len(data)):
    a, b = data[i]
    print(f"Case #{i + 1}: {a} + {b} = {a + b}")