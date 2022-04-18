import sys

count, data = int(sys.stdin.readline()), []
for i in range(0, count):
    data.append(sum((map(int, sys.stdin.readline().split()))))
for j in range(0, len(data)):
    print(f"Case #{j + 1}: {data[j]}")
