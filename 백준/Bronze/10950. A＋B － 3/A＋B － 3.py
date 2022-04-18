count, i, result = int(input()), 0, []
while i < count:
    result.append(list(map(int, input().split())))
    i = i + 1
list(map(lambda x: print(sum(x)), result))