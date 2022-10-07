import sys

s = sys.stdin.readline().strip()

list_0 = list(filter(lambda x: x != '', s.split('1')))
list_1 = list(filter(lambda x: x != '', s.split('0')))
print(len(list_0) if len(list_1) >= len(list_0) else len(list_1))
