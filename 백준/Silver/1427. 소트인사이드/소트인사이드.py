import sys

number = list(sys.stdin.readline().strip())
number.sort(reverse=True)
print("".join(number))