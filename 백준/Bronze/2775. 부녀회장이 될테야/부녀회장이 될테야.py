import sys

read = lambda: sys.stdin.readline().rstrip()
N = int(read())

for _ in range(N):
    floor = int(read())
    number = int(read())
    floorList = [i for i in range(1, number+1)]

    for i in range(floor):
        for j in range(1, number):
            floorList[j] += floorList[j-1]
    print(floorList[-1])