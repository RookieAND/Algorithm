import sys

read = sys.stdin.readline
money = int(read())

for _ in range(int(read())):
    cost, amount = map(int, read().split())
    money -= cost * amount

print('Yes' if money == 0 else 'No')