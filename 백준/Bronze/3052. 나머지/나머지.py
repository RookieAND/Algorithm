data = []
for _ in range(0, 10):
    data.append(int(input()) % 42)
print(len(set(data)))