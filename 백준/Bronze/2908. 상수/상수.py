a, b = map(lambda x: int(x[2]) * 100 + int(x[1]) * 10 + int(x[0]), input().split())
print(max(a, b))