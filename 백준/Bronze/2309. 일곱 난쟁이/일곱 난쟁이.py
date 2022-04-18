import sys
data = sorted([int(sys.stdin.readline().strip()) for i in range(9)])
total, find = sum(data), False
for i in range(0, len(data)):
    if find:
        break
    for j in range(i, len(data)):
        if total - (data[i] + data[j]) == 100:
            data.remove(data[j])
            data.remove(data[i])
            find = True
            break
list(map(lambda x: print(x), data))