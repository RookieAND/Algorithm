import sys

n, number = int(sys.stdin.readline()), 666
while n > 0:
    if '666' in str(number):
        n -= 1
        if n == 0:
            break
    number += 1
print(number)
