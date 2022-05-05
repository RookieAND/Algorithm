import sys

k = int(sys.stdin.readline())
data = []

for _ in range(k):
    price = int(sys.stdin.readline())
    if price == 0:
        data.pop()
    else:
        data.append(price)
print(sum(data))   