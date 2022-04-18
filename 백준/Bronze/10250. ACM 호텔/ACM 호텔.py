data = []
for _ in range(0, int(input())):
    h, w, n = map(int, input().split())
    if n % h != 0:
        data.append("{0}{1:0>2}".format((n % h), (n // h + 1)))
    else:
        data.append("{0}{1:0>2}".format(h, n // h))
list(map(lambda x: print(x), data))
