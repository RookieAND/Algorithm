data = list(map(int, input().split()))
print(sum(map(lambda x: x ** 2, data)) % 10)