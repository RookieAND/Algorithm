data = []
for num in range(1, 10001):
    data.append(num + sum(map(int, str(num))))
result = [i for i in range(1, 10001) if i not in data]
list(map(lambda x: print(x), result))