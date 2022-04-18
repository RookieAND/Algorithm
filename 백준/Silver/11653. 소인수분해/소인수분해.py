n, d, data = int(input()), 2, []
while n >= d:
    if n % d == 0:
        data.append(d)
        n = n // d
    else:
        d += 1
list(map(lambda x: print(x), data))