N, sumData = int(input()), 0
data = list(map(int, input().split()))
data.sort()
for num in data:
    sumData += num / data[len(data) - 1] * 100
print(sumData / len(data))