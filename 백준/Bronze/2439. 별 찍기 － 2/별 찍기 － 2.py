count = int(input())
list(map(lambda x: print(" " * (count - x) + "*" * x), range(1, count + 1)))