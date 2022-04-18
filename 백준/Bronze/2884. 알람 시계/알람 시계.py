H, M = map(int, input().split())
totalMin = H * 60 + M - 45
if totalMin < 0:
    totalMin += 24 * 60
print((totalMin // 60), (totalMin % 60))