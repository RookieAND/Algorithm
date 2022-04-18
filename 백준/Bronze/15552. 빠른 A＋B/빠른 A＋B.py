import sys
count, data = int(sys.stdin.readline()), []
for i in range(1, count + 1):
    data.append(map(int, sys.stdin.readline().split()))
list(map(lambda x: print(sum(x)), data))
