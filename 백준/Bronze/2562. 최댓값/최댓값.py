import sys
num, index = 0, 0
for i in range(0, 9):
    newNum = int(sys.stdin.readline())
    if newNum > num:
        num = newNum;
        index = i;
print(num)
print(index + 1)
