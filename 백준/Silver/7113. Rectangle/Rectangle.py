import sys
sys.setrecursionlimit(10**7)
m, n = map(int, sys.stdin.readline().split())
count = 0

def cut_rectangle(m, n):
    global count
    count += 1
    if m == n:
        return
    minVal = min(m, n)
    if m > minVal:
        return cut_rectangle(m - minVal, n)
    else:
        return cut_rectangle(m, n - minVal)

cut_rectangle(m, n)
print(count)
