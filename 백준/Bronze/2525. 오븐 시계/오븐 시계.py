a, b = map(int, input().split())
c = int(input())
totalMin = a * 60 + b + c
if totalMin >= 60 * 24:
    totalMin -= 60 * 24
print(totalMin // 60, totalMin % 60)