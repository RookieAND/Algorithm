data = []
while True:
    sumVal = sum(map(int, input().split()))
    if sumVal == 0: break
    data.append(sumVal)
list(map(lambda x: print(x), data))