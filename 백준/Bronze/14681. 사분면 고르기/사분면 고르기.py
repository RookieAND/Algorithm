x = int(input())
y = int(input())
qdr = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
print(qdr.index((x // abs(x), y // abs(y))) + 1)
